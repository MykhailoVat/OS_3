# physicalMemory

from singleton import Singleton

class Frame:
    def __init__(self, size, base):
        self.size = size
        self.base = base

class PhysicalMemory(metaclass=Singleton):
    def __init__(self, capacity, frame_size):
        self.frame_list = []
        self.frame_count = capacity // frame_size

        base = 0x0000
        for i in range(self.frame_count):
            frame = Frame(frame_size, base)
            self.frame_list.append(frame)
            base += frame_size

    def get_frame_count(self):
        return self.frame_count
