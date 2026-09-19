# process
from pageTable import PageTable

class Process:
    def __init__(self, name, accesses, data, page_size):
        amount = (len(data) + page_size - 1) // page_size
        self.table = PageTable(amount)

        self.name = name
        self.accesses = accesses
        self._current_address = 0

    def get_current_address(self):
        if self._current_address >= len(self.accesses):
            return None

        address = self.accesses[self._current_address]
        self._current_address += 1
        return address
