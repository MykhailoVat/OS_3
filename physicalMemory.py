class Frame:
    def __init__(self, size, base):
        self.size = size
        self.base = base

class PhysicalMemory:
    def __init__(self, capacity = 65536, frame_size = 4096): #64 and 4 KiB
        self.frame_list = []

        frame_count = capacity // frame_size
        base = 0x0000
        for i in range(frame_count):
            frame = Frame(frame_size, base)
            self.frame_list.append(frame)
            base += frame_size
