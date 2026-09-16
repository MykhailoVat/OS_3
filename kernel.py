# kernel

import asyncio

class Kernel:
    def __init__(self, mmu):
        self.mmu = mmu
        self.processes_list = []
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

            current_process = self.processes_list[self.current_process_id]
            v_address = current_process.get_current_address()

            if v_address is None:
                self.processes_list.pop(self.current_process_id)
                continue

            # not mapped at this point of development
            mapped_address = self.mmu.map_address(v_address)
            print(mapped_address)

            # value 1 for slow stdout demonstration
            await asyncio.sleep(0)


    def append_process(self, process):
        self.processes_list.append(process)
        self.process_count += 1
