# process
import random

from opt.func.generate_access import generate_access
from pageTable import PageTable
from workingSet import WorkingSet


class Process:
    def __init__(self, pid, name, data, page_size, amount):
        pages_number = (len(data) + page_size - 1) // page_size
        self.data_size = len(data)
        self.table = PageTable(pages_number)
        # MAGIC
        self.working_set = WorkingSet(3,pages_number)

        self.pid = pid
        self.name = name
        self.access_number = amount
        self.access_count = 0
        self.current_access = None

    def get_access(self):
        if self.current_access is None:
            if self.access_count >= self.access_number:
                return None

            self.current_access = generate_access(self.data_size)

        return self.current_access

    def point_next(self):
        self.current_access = None
        self.access_count += 1

    def get_name(self):
        return self.name

    def get_table(self):
        return self.table
                             #not shadowing 'bool'
    def page_set_p(self, page, bowl):
        self.table.set_p(page, bowl)

    def page_set_r(self, page, bowl):
        self.table.set_r(page, bowl)

    def page_set_m(self, page, bowl):
        self.table.set_m(page, bowl)

    def page_set_ppn(self, page, value):
        self.table.set_ppn(page, value)
