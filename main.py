#main

import asyncio

from opt.obj.data import fs_data
from opt.func.create_process import create_process

from fileSystem import FileSystem
from physicalMemory import PhysicalMemory
from mmu import MMU
from kernel import Kernel

# CONSTANTS
MEMORY_SIZE = 64
PAGE_SIZE = FRAME_SIZE = 4

MIN_ACCESSES = 5
MAX_ACCESSES = 15

async def run_system():
    mmu = MMU(PAGE_SIZE)
    memory = PhysicalMemory(MEMORY_SIZE, FRAME_SIZE)
    fs = FileSystem(fs_data)

    kernel = Kernel(mmu, fs, memory)

    kernel.start()

    while True:
        kernel.create_process(MIN_ACCESSES, MAX_ACCESSES, fs_data, PAGE_SIZE)
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(run_system())