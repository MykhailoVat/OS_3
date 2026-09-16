#main

from time import sleep
import random
import asyncio

from process import Process
from mmu import MMU
from kernel import Kernel

def create_process():
    addresses = random.choice([
        ['0x1000', '0x2000', '0x3000'],
        ['0xABCD', '0x1234', '0x5678'],
        ['0x1111', '0x2222', '0x3333']
    ])

    return Process(addresses)

async def run_system():
    mmu = MMU()
    kernel = Kernel(mmu)

    kernel.start()

    while True:
        kernel.append_process(create_process())
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(run_system())