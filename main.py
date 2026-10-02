# main

from opt.obj.data import fs_data
import opt.consts

from fileSystem import FileSystem
from physicalMemory import PhysicalMemory
from mmu import MMU
from kernel import Kernel

def run_system():
    mmu = MMU(opt.consts.PAGE_SIZE)
    memory = PhysicalMemory(opt.consts.MEMORY_SIZE, opt.consts.FRAME_SIZE)
    fs = FileSystem(fs_data)

    kernel = Kernel(mmu, fs, memory)

    kernel.run()

if __name__ == "__main__":
    run_system()
