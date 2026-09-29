#main

import asyncio

from opt.obj.data import fs_data

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
    kernel.set_proc_spawn_info(fs_data, MIN_ACCESSES, MAX_ACCESSES, PAGE_SIZE)

    kernel.start()


if __name__ == "__main__":
    asyncio.run(run_system())