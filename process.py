# process
from pageTable import PageTable

class Process:
    def __init__(self, name, accesses, data, page_size):
        amount = (len(data) + page_size - 1) // page_size
        self.table = PageTable(amount)

        self.name = name
        self.accesses = accesses
        self.current_access = 0

    def point_next(self):
        self.current_access +=1

    def get_current_access(self):
        if self.current_access >= len(self.accesses):
            return None

        access = self.accesses[self.current_access]
        return access

    def get_name(self):
        return self.name

    def get_table(self):
        return self.table

    def page_set_p(self, page, value):
        self.table.set_p(page, value)

    def page_set_ppn(self, page, value):
        self.table.set_ppn(page, value)
