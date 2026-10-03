# physicalMemory

from opt.obj.singleton import Singleton

class Frame:
    def __init__(self, size, base):
        self.size = size
        self.base = base
        self.data = [0 for _ in range(size)]

    def insert_data(self, data):
        self.data = data

    def free(self):
        self.data = [0 for _ in range(self.size)]


class PhysicalMemory(metaclass=Singleton):
    def __init__(self, capacity, frame_size):
        self.frame_list = []
        self.frame_count = capacity // frame_size
        self.metadata = {}

        base = 0x0000
        for i in range(self.frame_count):
            frame = Frame(frame_size, base)
            self.frame_list.append(frame)
            base += frame_size

            self.metadata[i] = None

    def read(self, frame_id, offset, time):
        self.metadata[frame_id]["last_ref"] = time
        return self.frame_list[frame_id].data[offset]

    def write(self, frame_id, offset, data, time):
        self.metadata[frame_id]["last_ref"] = time
        self.frame_list[frame_id].data[offset] = data

    def write_frame(self, frame_id, data, ptr_pte, pid, v_page, time):
        self.metadata[frame_id] = {
            "ptr_pte": ptr_pte,
            "pid": pid,
            "v_page": v_page,
            "last_ref": time
        }

        frame = self.frame_list[frame_id]
        frame.insert_data(data)

        #print
        print(frame.data)

    def find_free_frame(self):
        for i in range(self.frame_count):
            if self.metadata[i] is None:
                return i

        return None

    def free_frame(self, frame_id):
        self.frame_list[frame_id].free()

        self.metadata[frame_id]["ptr_pte"]["P"] = False
        self.metadata[frame_id]["ptr_pte"]["R"] = False
        self.metadata[frame_id]["ptr_pte"]["M"] = False
        self.metadata[frame_id]["ptr_pte"]["PPN"] = None

        self.metadata[frame_id] = None

    def get_frame_count(self):
        return self.frame_count

    def get_frame_content(self, frame_id):
        return self.frame_list[frame_id].data

    def get_metadata(self):
        return self.metadata

    def m_get_bit(self, frame_id, bit):
        return self.metadata[frame_id]["ptr_pte"][bit]

    def m_get_pid(self, frame_id):
        return self.metadata[frame_id]["pid"]

    def m_get_page_id(self, frame_id):
        return self.metadata[frame_id]["v_page"]

    def m_get_active_frames(self):
        active = []

        for frame_id in self.metadata:
            if self.metadata[frame_id] is not None:
                active.append(frame_id)

        return active

    def m_get_process_frames(self, pid):
        frames = []

        for frame_id, metadata in self.metadata.items():
            if metadata is not None and metadata["pid"] == pid:
                frames.append(frame_id)

        return frames

    def m_set_bit(self, frame_id, bit, value):
        self.metadata[frame_id]["ptr_pte"][bit] = value
