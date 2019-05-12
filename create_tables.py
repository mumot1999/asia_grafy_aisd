import matplotlib.pyplot as plt
from helpers import get_measurements, save_measurements
import numpy as np
import statistics



measurements = get_measurements('dane.json')

import jinja2
import imgkit

loader = jinja2.FileSystemLoader('.')
env = jinja2.Environment(loader=loader)

template = env.get_template('table.html')
import math
for name, datas in measurements.items():
    items = []

    for d in datas:
        items.append({
            'elements': d[0],
            'time': d[1],
            'error': d[2],
        })

    html = template.render(items=items)
    imgkit.from_string(html, 'tables/{}.jpg'.format(name))