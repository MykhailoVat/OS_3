# kernel

from time import (sleep)
import asyncio

from opt.obj.accessType import AccessType
from opt.obj.pageFault import PageFault
from opt.obj.singleton import Singleton
from opt.func.create_process import create_process
from opt.obj.pidAllocator import PIDAllocator

class Kernel(metaclass=Singleton):

    def __init__(self, mmu, fs, memory):
        # components
        self.mmu = mmu
        self.fs = fs
        self.memory = memory

        # tools
        self.allocator = PIDAllocator()

        # state
        self.processes_list = []
        self.current_process = None
        self.current_process_id = 0
        self.task_run = None

        # process spawn info (add via special method)
        self.fs_data = None
        self.min_acc = None
        self.max_acc = None
        self.page_size = None

    def set_proc_spawn_info(self, data, min_acc, max_acc, page_size):
        self.fs_data = data
        self.min_acc = min_acc
        self.max_acc = max_acc
        self.page_size = page_size

    def start(self):
        self.task_run = asyncio.create_task(self.run())

    async def run(self):
        while True:
            if not self.processes_list:
                self.create_process(self.min_acc,
                                    self.max_acc,
                                    self.fs_data,
                                    self.page_size)
                continue

            self.current_process = self.processes_list[self.current_process_id]

            access = self.current_process.get_current_access()

            if access is None:
                self.processes_list.pop(self.current_process_id)
                continue

            v_address = access.address
            operation = access.operation

            try:
                frame_id, offset, v_page = self.mmu.map_address(
                    v_address,
                    self.current_process.get_table()
                )

                data = None
                if access.operation == AccessType.READ:
                    data = self.memory.read_data(frame_id, offset)
                    self.current_process.page_set_r(v_page, True)
                elif access.operation == AccessType.WRITE:
                    self.memory.write_data(frame_id, offset, access.value)
                    self.current_process.page_set_r(v_page, True)
                    self.current_process.page_set_m(v_page, True)

                # print
                print(f'process_name: {self.current_process.name}')
                print(f'PID: {self.current_process.pid}')
                print(f'v_address: {v_address}')
                print(f'p_address: {frame_id} + {offset}')
                print(f'operation: {operation}')
                print(data)
                print(" ")

                self.current_process.point_next()

            except PageFault as fault:
                self.handle_page_fault(fault.v_page)

            # value for slow stdout demonstration
            sleep(1)

    def handle_page_fault(self, v_page):
        page_size = self.mmu.get_page_size()
        name = self.current_process.get_name()

        offset = page_size * v_page
        data = self.fs.read_data(name, offset, page_size)

        frame_id = self.memory.find_free_frame()

        if frame_id is None:
            print("No free memory")
            return

        self.memory.fill_frame(frame_id, data)

        self.current_process.page_set_p(v_page, True)
        self.current_process.page_set_ppn(v_page, frame_id)


    def create_process(self, min_acc, max_acc, fs_data, p_size):
        pid = self.allocator.allocate()
        process = create_process(pid, min_acc, max_acc,fs_data, p_size)
        self.processes_list.append(process)