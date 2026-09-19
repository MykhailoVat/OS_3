# pageTable

class PageTable:
    def __init__(self, amount):
        self.pages = [
            {"P": False, "R": False, "M": False, "PPN": None}
            for _ in range(amount)
        ]