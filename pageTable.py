# pageTable

class PageTable:
    def __init__(self, amount):
        self.pages = [
            {"P": False, "R": False, "M": False, "PPN": None}
            for _ in range(amount)
        ]

    def set_p(self, page, value):
        self.pages[page]["P"] = value

    def set_ppn(self, page, value):
        self.pages[page]["PPN"] = value

    def get_p(self, page):
        return self.pages[page]["P"]