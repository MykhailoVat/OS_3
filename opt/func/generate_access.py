import random

from opt.obj.memoryAccess import MemoryAccess
from opt.obj.accessType import AccessType

def generate_access(ws_entries, pages_number, page_size):
    # MAGIC
    if random.random() < 0.9:
        page = random.choice(ws_entries)
    else:
        page = random.randrange(pages_number)

    offset = random.randrange(page_size)
    address = page * page_size + offset

    # MAGIC
    access_type = random.choices(
        [AccessType.READ, AccessType.WRITE],
        weights=[0.7, 0.3]
    )[0]

    return MemoryAccess(address, access_type)