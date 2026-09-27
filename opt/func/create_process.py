import random
from process import Process
from opt.func.generate_access import generate_accesses

def create_process(pid,min_acc, max_acc, fs_data, page_size):
    name = random.choice([*fs_data.keys()])
    amount = random.randint(min_acc, max_acc)
    accesses = generate_accesses(len(fs_data[name]),amount)

    return Process(pid, name, accesses, fs_data[name], page_size)
