# process
import opt.consts

from opt.func.generate_access import generate_access
from pageTable import PageTable
from workingSet import WorkingSet


class Process:
    def __init__(self, pid, name, data, page_size, amount):
        self.page_size = page_size
        self.pages_number = (len(data) + page_size - 1) // page_size
        self.table = PageTable(self.pages_number)

        self.working_set = WorkingSet(opt.consts.WS_ENTRIES, self.pages_number)

        self.pid = pid
        self.name = name
        self.access_number = amount
        self.access_count = 0
        self.current_access = None

    def get_access(self):
        if self.current_access is None:
            if self.access_count >= self.access_number:
                return None

            self.current_access = generate_access(
                self.working_set.get_entries(),
                self.pages_number,
                self.page_size
            )

            print(f"PID={self.pid}: working set -> {self.working_set.get_entries()}")

        return self.current_access

    def point_next(self):
        self.current_access = None
        self.access_count += 1

        if self.access_count % opt.consts.WS_UPD_INTERVAL == 0:
            self.working_set.update()

    def end(self):


    def get_name(self):
        return self.name

    def get_pid(self):
        return self.pid

    def get_table(self):
        return self.table

    def get_pte(self, page):
        return self.table.get_pte(page)
                             #not shadowing 'bool'
    def page_set_p(self, page, bowl):
        self.table.set_p(page, bowl)

    def page_set_r(self, page, bowl):
        self.table.set_r(page, bowl)

    def page_set_m(self, page, bowl):
        self.table.set_m(page, bowl)

    def page_set_ppn(self, page, value):
        self.table.set_ppn(page, value)
