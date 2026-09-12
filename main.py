#main

from time import sleep
import random
import asyncio

from process import Process
from mmu import MMU
from kernel import Kernel

async def run_system():
    process1 = Process([0x1000, 0x2000, 0x3000])
    process2 = Process([0xABCD, 0x1234, 0x5678])
    process3 = Process([0x1111, 0x2222, 0x3333])

    processes = [process1, process2, process3]

    mmu = MMU()
    kernel = Kernel(mmu)

    asyncio.create_task(kernel.run())

    while True:
        kernel.append_process(random.choice(processes))
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(run_system())