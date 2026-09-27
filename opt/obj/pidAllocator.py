class PIDAllocator:
    def __init__(self):
        self.next_pid = 0

    def allocate(self):
        pid = self.next_pid
        self.next_pid += 1
        return pid