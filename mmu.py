# mmu

from opt.singleton import Singleton
from opt.pageFault import PageFault

class MMU(metaclass=Singleton):
    def __init__(self, page_size):
        self.page_size = page_size

    def map_address(self, v_address, table):
        v_page = v_address // self.page_size
        offset = v_address % self.page_size

        if not table[v_page]["P"]:
            raise PageFault(v_page)

        return [v_page, offset]
