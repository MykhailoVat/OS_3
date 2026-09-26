# fileSystem

from opt.obj.singleton import Singleton

class FileSystem(metaclass=Singleton):
    def __init__(self, data):
        self.data = data

    def read_data(self, file, offset, bites):
        file_data = self.data[file]
        return file_data[offset : offset + bites]