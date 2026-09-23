# physicalMemory

from opt.singleton import Singleton

class Frame:
    def __init__(self, size, base):
        self.size = size # do i need this?
        self.base = base # do i need this?
        self.data = [0 for _ in range(size)]

    def insert_data(self, data):
        self.data = data


class PhysicalMemory(metaclass=Singleton):
    def __init__(self, capacity, frame_size):
        self.frame_list = []
        self.frame_count = capacity // frame_size

        base = 0x0000
        for i in range(self.frame_count):
            frame = Frame(frame_size, base)
            self.frame_list.append(frame)
            base += frame_size

    def fill_frame(self, frame_id, data):
        frame = self.frame_list[frame_id]
        frame.insert_data(data)
        print(frame.data)

    def get_frame_count(self):
        return self.frame_count
