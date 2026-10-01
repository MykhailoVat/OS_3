# workingSet
import random

class WorkingSet:
    def __init__(self, entries_number, pages_number):
        self.entries_number = entries_number
        self.pages_number = pages_number

        self.set = random.sample(range(pages_number), entries_number)

    def update(self):
        self.set = random.sample(range(self.pages_number), self.entries_number)

    def get_entries(self):
        return self.set
