# process
from pageTable import PageTable

class Process:
    def __init__(self, name, v_addresses, page_size):
        amount = (len(v_addresses) + page_size - 1) // page_size
        self.table = PageTable(amount)

        self.name = name
        self._v_addresses = v_addresses
        self._current_address = 0

    def get_current_address(self):
        if self._current_address >= len(self._v_addresses):
            return None

        address = self._v_addresses[self._current_address]
        self._current_address += 1
        return address
