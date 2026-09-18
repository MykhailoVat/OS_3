# mmu

from opt.singleton import Singleton

class MMU(metaclass=Singleton):
    def __init__(self):
        pass

    def map_address(self, v_address):
        return v_address