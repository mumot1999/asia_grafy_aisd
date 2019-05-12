import time
import statistics


def measure_time(method, *args, **kwargs):
    time_measurements = []
    for i in range(5):
        time_start = time.time()
        method(*args, **kwargs)
        time_end = time.time()
        time_measurements.append(time_end - time_start)

    return statistics.mean(time_measurements)
