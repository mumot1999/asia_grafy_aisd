import random


def random_list(count):
    data = [i for i in range(count)]
    random.shuffle(data)
    return data
