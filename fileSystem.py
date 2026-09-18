# fileSystem

from singleton import Singleton

class FileSystem(metaclass=Singleton):
    def __init__(self):
        self.data = []