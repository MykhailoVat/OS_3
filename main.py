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

QUANTUM_SIZE = 5
SPAWN_INTERVAL = 8

async def run_system():
    mmu = MMU(PAGE_SIZE)
    memory = PhysicalMemory(MEMORY_SIZE, FRAME_SIZE)
    fs = FileSystem(fs_data)

    kernel = Kernel(mmu, fs, memory)
    kernel.set_proc_gen_info(fs_data, MIN_ACCESSES, MAX_ACCESSES, PAGE_SIZE)
    kernel.set_tick_info(QUANTUM_SIZE, SPAWN_INTERVAL)

    kernel.run()


if __name__ == "__main__":
    asyncio.run(run_system())