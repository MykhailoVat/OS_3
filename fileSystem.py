# fileSystem

from opt.singleton import Singleton

class FileSystem(metaclass=Singleton):
    def __init__(self, data):
        self.data = data