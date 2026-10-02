# fileSystem

from opt.obj.singleton import Singleton

class FileSystem(metaclass=Singleton):
    def __init__(self, data):
        self.data = data
        self.pages = {}

    def read_data(self, file, offset, bites):
        file_data = self.data[file]
        return file_data[offset : offset + bites]

    def read_page(self, pid, page_number):
        return self.pages.get((pid, page_number))

    def write_page(self, pid, page_number, data):
        self.pages[(pid, page_number)] = data

    def delete_pages(self, pid):
        for key in list(self.pages):
            if key[0] == pid:
                del self.pages[key]