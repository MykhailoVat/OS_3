# mmu

from opt.singleton import Singleton

class MMU(metaclass=Singleton):
    def __init__(self, page_size):
        self.page_size = page_size

    def map_address(self, v_address, table):
        virtual_page = v_address // self.page_size
        offset = v_address % self.page_size

        return [virtual_page, offset]