# process
from pageTable import PageTable

class Process:
    def __init__(self, name, accesses, data, page_size):
        amount = (len(data) + page_size - 1) // page_size
        self.table = PageTable(amount)

        self.name = name
        self.accesses = accesses
        self._current_address = 0

    def point_next(self):
        self._current_address +=1

    def get_current_address(self):
        if self._current_address >= len(self.accesses):
            return None

        address = self.accesses[self._current_address]
        return address

    def get_name(self):
        return self.name

    def set_table_p(self, page, value):
        self.table.pages[page]["P"] = value

    def set_table_ppn(self, page, value):
        self.table.pages[page]["PPN"] = value
