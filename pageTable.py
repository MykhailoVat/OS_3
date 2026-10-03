# pageTable

class PageTable:
    def __init__(self, amount):
        self.content = [
            {"P": False, "R": False, "M": False, "PPN": None}
            for _ in range(amount)
        ]

    def get_pages(self):
        return self.content

    def get_pte(self, page):
        return self.content[page]

    def set_p(self, page, bowl):
        self.content[page]["P"] = bowl

    def set_r(self, page, bowl):
        self.content[page]["R"] = bowl

    def set_m(self, page, bowl):
        self.content[page]["M"] = bowl

    def set_ppn(self, page, value):
        self.content[page]["PPN"] = value

    def get_p(self, page):
        return self.content[page]["P"]

    def get_ppn(self, page):
        return self.content[page]["PPN"]