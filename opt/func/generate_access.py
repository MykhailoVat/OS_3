import random

from opt.obj.memoryAccess import MemoryAccess
from opt.obj.accessType import AccessType

def generate_accesses(data_size, amount):
    accesses = []

    current = random.randrange(data_size)

    for _ in range(amount):
        access_type = random.choices(
            [AccessType.READ, AccessType.WRITE],
            weights=[0.7, 0.3]
        )[0]

        accesses.append(
            MemoryAccess(current, access_type)
        )

        if random.random() < 0.8:
            current += random.choice([-1, 0, 1])
            current = max(0, min(data_size - 1, current))
        else:
            current = random.randrange(data_size)

    return accesses