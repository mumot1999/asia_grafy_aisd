from krawedz import run as run_krawedz
from macierz import run as run_macierz
from nastepnik import run as run_nastepniki
from helpers import save_measurements

import numpy as np
import statistics


elements = [n*10 for n in range(1,11)]


functions = {
    "krawedz": run_krawedz,
    "macierz": run_macierz,
    "nastepnik": run_nastepniki

}
clear_measurements = lambda: {e: [] for e in elements}
measurements = {}

for name, function in functions.items():
    measurements['{}_sort_top_del'.format(name)] = clear_measurements()
    measurements['{}_sort_top_dfs'.format(name)] = clear_measurements()

for name, function in functions.items():
    for e in elements:
        for _ in range(10):
            pomiary = function(e)
            while not pomiary:
                pomiary = function(e)
            measurements['{}_sort_top_del'.format(name)][e].append(pomiary['sort_top_del'])
            measurements['{}_sort_top_dfs'.format(name)][e].append(pomiary['sort_top_dfs'])

for m in measurements:
    save_measurements(m, measurements[m])


for measure_name, functions_measurements in measurements.items():
    x = functions_measurements.keys()
    y = list(map(lambda x: statistics.mean(x), functions_measurements.values()))
    e = list(map(lambda x: np.std(x), functions_measurements.values()))

    datas = list(zip(x,y,e))

    save_measurements(measure_name, datas, 'dane.json')
