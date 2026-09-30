# main

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

SPAWN_INTERVAL = 8
QUANTUM_SIZE = 4

SPAWN_CHANCE = 0.9

MAX_PROCS = 4


async def run_system():
    mmu = MMU(PAGE_SIZE)
    memory = PhysicalMemory(MEMORY_SIZE, FRAME_SIZE)
    fs = FileSystem(fs_data)

    kernel = Kernel(mmu, fs, memory)
    kernel.set_consts(
        fs_data,
        MIN_ACCESSES,
        MAX_ACCESSES,
        PAGE_SIZE,
        SPAWN_INTERVAL,
        QUANTUM_SIZE,
        SPAWN_CHANCE,
        MAX_PROCS
    )

    kernel.run()


if __name__ == "__main__":
    asyncio.run(run_system())
