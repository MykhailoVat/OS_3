# process

class Process:
    def __init__(self, v_addresses):
        self._v_addresses = v_addresses
        self._current_address = 0

    def get_current_address(self):
        if self._current_address >= len(self._v_addresses):
            return None
        address = self._v_addresses[self._current_address]
        self._current_address += 1
        return address
