#main

from time import sleep
import random
import asyncio

from opt.data import fs_data
from opt.generate_access import generate_accesses

from fileSystem import FileSystem
from physicalMemory import PhysicalMemory
from process import Process
from mmu import MMU
from kernel import Kernel

# CONSTANTS
MEMORY_SIZE = 128
PAGE_SIZE = FRAME_SIZE = 4

MIN_ACCESSES = 5
MAX_ACCESSES = 15

def create_process():
    name = random.choice([*fs_data.keys()])
    amount = random.randint(MIN_ACCESSES,MAX_ACCESSES)
    accesses = generate_accesses(len(fs_data[name]),amount)

    return Process(name, accesses, PAGE_SIZE)

async def run_system():
    mmu = MMU(PAGE_SIZE)
    memory = PhysicalMemory(MEMORY_SIZE, FRAME_SIZE)
    fs = FileSystem(fs_data)

    kernel = Kernel(mmu, fs, memory)

    kernel.start()

    while True:
        kernel.append_process(create_process())
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(run_system())