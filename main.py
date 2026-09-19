#main

from time import sleep
import random
import asyncio

from opt.data import fs_data
from fileSystem import FileSystem
from process import Process
from mmu import MMU
from kernel import Kernel

# CONSTANTS
MEMORY_SIZE = 512
PAGE_SIZE = 8

def create_process():
    return random.choice([
        Process("proc1",['0x1000', '0x2000', '0x3000']),
        Process("proc2",['0xABCD', '0x1234', '0x5678']),
        Process("proc3",['0x1111', '0x2222', '0x3333'])
    ])

async def run_system():
    mmu = MMU()
    fs = FileSystem(fs_data)

    kernel = Kernel(mmu)

    kernel.start()

    while True:
        kernel.append_process(create_process())
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(run_system())