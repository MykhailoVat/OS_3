import random

from opt.obj.memoryAccess import MemoryAccess
from opt.obj.accessType import AccessType

def generate_access(data_size):
    address = random.randrange(data_size)

    # MAGIC
    access_type = random.choices(
        [AccessType.READ, AccessType.WRITE],
        weights=[0.7, 0.3]
    )[0]

    return MemoryAccess(address, access_type)