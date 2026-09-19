#main

from time import sleep
import random
import asyncio

from opt.data import fs_data
from opt.generate_access import generate_accesses

from fileSystem import FileSystem
from process import Process
from mmu import MMU
from kernel import Kernel

# CONSTANTS
MEMORY_SIZE = 512
PAGE_SIZE = 8

MIN_ACCESSES = 5
MAX_ACCESSES = 15

def create_process():
    name = random.choice([*fs_data.keys()])
    amount = random.randint(MIN_ACCESSES,MAX_ACCESSES)
    accesses = generate_accesses(len(fs_data[name]),amount)
    return Process(name, accesses)

async def run_system():
    mmu = MMU()
    fs = FileSystem(fs_data)

    kernel = Kernel(mmu, fs)

    kernel.start()

    while True:
        kernel.append_process(create_process())
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(run_system())