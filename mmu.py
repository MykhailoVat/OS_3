# mmu

from opt.obj.singleton import Singleton
from opt.obj.pageFault import PageFault

class MMU(metaclass=Singleton):
    def __init__(self, page_size):
        self.page_size = page_size

    def map_address(self, v_address, table):
        v_page = v_address // self.page_size
        offset = v_address % self.page_size

        if not table.get_p(v_page):
            raise PageFault(v_page)

        frame_id = table.get_ppn(v_page)

        return [frame_id, offset, v_page]

    def get_page_size(self):
        return self.page_size
