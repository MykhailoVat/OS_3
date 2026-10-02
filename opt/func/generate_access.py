import random

import opt.consts

from opt.obj.memoryAccess import MemoryAccess
from opt.obj.accessType import AccessType

def generate_access(ws_entries, pages_number, page_size):
    if random.random() < opt.consts.CHANCE_LOCAL:
        page = random.choice(ws_entries)
    else:
        page = random.randrange(pages_number)

    offset = random.randrange(page_size)
    address = page * page_size + offset

    access_type = random.choices(
        [AccessType.READ, AccessType.WRITE],
        weights=[opt.consts.READ_WEIGHT, opt.consts.WRITE_WEIGHT]
    )[0]

    return MemoryAccess(address, access_type)