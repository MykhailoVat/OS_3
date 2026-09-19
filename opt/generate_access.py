import random


def generate_accesses(data_size, amount):
    addresses = []

    current = random.randrange(data_size)

    for _ in range(amount):
        addresses.append(current)

        if random.random() < 0.8:
            # локальний доступ
            current += random.choice([-1, 0, 1])
            current = max(0, min(data_size - 1, current))
        else:
            # стрибок в іншу область
            current = random.randrange(data_size)

    return addresses