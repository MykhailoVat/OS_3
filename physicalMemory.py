# physicalMemory

from opt.obj.singleton import Singleton

class Frame:
    def __init__(self, size, base):
        self.base = base
        self.is_free = True
        self.data = [0 for _ in range(size)]

    def insert_data(self, data):
        self.data = data

    def set_free(self, status):
        self.is_free = status


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
        frame.set_free(False)

        #print
        print(frame.data)

    def read_data(self, frame_id, offset):
        return self.frame_list[frame_id].data[offset]

    def find_free_frame(self):
        for i in range(self.frame_count):
            if self.frame_list[i].is_free is True:
                return i

        return None

    def get_frame_count(self):
        return self.frame_count
