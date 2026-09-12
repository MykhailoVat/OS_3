from time import sleep
from process import Process
from mmu import MMU

def kernel_mock():
    process1 = Process([0x1000, 0x2000, 0x3000])
    process2 = Process([0xABCD, 0x1234, 0x5678])
    process3 = Process([0x1111, 0x2222, 0x3333])

    mmu = MMU()

    processes = [process1, process2, process3]

    for process in processes:
        while True:
            address = process.get_current_address()
            if address is None:
                break
            mmu.map_address(address)
        sleep(5)


if __name__ == "__main__":
    kernel_mock()