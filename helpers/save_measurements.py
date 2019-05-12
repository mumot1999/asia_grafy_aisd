import json


def save_measurements(name, measurements, file_name='pomiary.json'):

    file_measurements = {}
    try:
        with open(file_name, 'r') as file:
            if file.readable():
                file_measurements = json.loads(file.read())
    except FileNotFoundError:
        print('Tworzenie nowego pliku pomiary.json')

    with open(file_name, 'w') as file:
        file_measurements[name] = measurements
        json.dump(file_measurements, file)
