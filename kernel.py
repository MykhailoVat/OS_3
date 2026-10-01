# kernel
import random
from time import (sleep)
from collections import deque

from opt.obj.accessType import AccessType
from opt.obj.pageFault import PageFault
from opt.obj.singleton import Singleton
from opt.obj.pidAllocator import PIDAllocator
from opt.obj.sequenceResult import SequenceResult

from opt.func.create_process import create_process


class Kernel(metaclass=Singleton):

    def __init__(self, mmu, fs, memory):
        # main components
        self.mmu = mmu
        self.fs = fs
        self.memory = memory

        # tools
        self.allocator = PIDAllocator()

        # state
        self.queue = deque()
        self.process_count = 0
        self.current_process = None

        # ticks
        self.tick = 0
        self.quantum_tick = 0

        # CONSTS TO SET

        self.spawn_interval = None
        self.quantum_size = None

        self.spawn_chance = None

        self.process_limit = None

        self.fs_data = None
        self.min_acc = None
        self.max_acc = None
        self.page_size = None

    def set_consts(
            self,
            data,
            min_acc,
            max_acc,
            page_size,
            spawn_interval,
            quantum_size,
            spawn_chance,
            process_limit
    ):
        self.fs_data = data
        self.min_acc = min_acc
        self.max_acc = max_acc
        self.page_size = page_size
        self.spawn_interval = spawn_interval
        self.quantum_size = quantum_size
        self.spawn_chance = spawn_chance
        self.process_limit = process_limit

    def run(self):
        while True:
            if self.tick % self.spawn_interval == 0:
                if self.process_count >= self.process_limit:
                    print("PROCESS COUNT LIMIT REACHED")
                    sleep(1)
                    continue

                self.s_create_process(
                    self.min_acc,
                    self.max_acc,
                    self.fs_data,
                    self.page_size
                )

            if not self.queue:
                print("NO PROCESS TO DO")
                self.tick += 1
                continue

            print(
                f"tick={self.tick}, "
                f"quantum={self.quantum_tick}, "
                f"queue={[p.pid for p in self.queue]}"
            )

            access_res = self.access_sequence()

            if access_res == SequenceResult.PROCESS_FINISHED:
                self.queue.popleft()
                self.process_count -= 1
                self.quantum_tick = 0
                continue

            self.tick += 1
            self.quantum_tick += 1

            if self.quantum_tick >= self.quantum_size:
                self.s_switch_process()
                self.quantum_tick = 0

            sleep(0.1)

    def access_sequence(self):
        self.current_process = self.queue[0]

        access = self.current_process.get_access()

        if access is None:
            return SequenceResult.PROCESS_FINISHED

        v_address = access.address

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

            print(f'process_name: {self.current_process.name}')
            print(f'PID: {self.current_process.pid}')
            print(f'v_address: {v_address}')
            print(f'p_address: {frame_id} + {offset}')
            print(f'operation: {access.operation}')
            print(data)
            print(" ")

            self.current_process.point_next()

            return SequenceResult.ACCESS_DONE

        except PageFault as fault:
            self.handle_page_fault(fault.v_page)
            return SequenceResult.PAGE_FAULT

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

    def s_create_process(self, min_acc, max_acc, fs_data, p_size):
        if random.random() < self.spawn_chance:
            pid = self.allocator.allocate()
            process = create_process(pid,
                                     min_acc,
                                     max_acc,
                                     fs_data,
                                     p_size)

            self.queue.append(process)
            self.process_count += 1

    def s_switch_process(self):
        process = self.queue.popleft()
        self.queue.append(process)

