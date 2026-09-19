# kernel

import asyncio

from opt.pageFault import PageFault
from opt.singleton import Singleton

class Kernel(metaclass=Singleton):

    def __init__(self, mmu, fs, memory):
        self.mmu = mmu
        self.fs = fs
        self.memory = memory

        self.processes_list = []
        self.current_process = None
        self.current_process_id = 0

        self.process_count = 0
        self.task = None

    def start(self):
        self.task = asyncio.create_task(self.run())

    async def run(self):
        while True:
            if not self.processes_list:
                await asyncio.sleep(0.1)
                continue

            self.current_process = self.processes_list[self.current_process_id]
            v_address = self.current_process.get_current_address()

            if v_address is None:
                self.processes_list.pop(self.current_process_id)
                continue

            try:
                p_address = self.mmu.map_address(
                    v_address,
                    self.current_process.table.pages
                )
            except PageFault as fault:
                self.handle_page_fault()

            # print
            print(f'process_name: {self.current_process.name}')
            print(f'address: {v_address}')

            # value for slow stdout demonstration
            await asyncio.sleep(1)


    def append_process(self, process):
        self.processes_list.append(process)
        self.process_count += 1

    def handle_page_fault(self):
        print("Page Fault")