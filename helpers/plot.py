import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

import json


def get_measurements(file='measurements/pomiary.json'):
    with open(file, 'r') as file:
        measurements = file.read()

    return json.loads(measurements)


def add_data(data, label=''):
    plt.plot(data.keys(), data.values(), label=label)


def create_plot(title, xlabel='Time', ylabel='Elements', y_scale=None):
    plt.legend()
    plt.title(title)
    if y_scale:
        plt.yscale(y_scale)
    plt.ylabel(xlabel)
    plt.xlabel(ylabel)
    plt.grid(True)
    plt.savefig('plots/'+title)
    plt.clf()
