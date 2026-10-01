import random
from process import Process

def create_process(pid, min_acc, max_acc, fs_data, page_size):
    name = random.choice([*fs_data.keys()])
    amount = random.randint(min_acc, max_acc)

    return Process(pid, name, fs_data[name], page_size, amount)
