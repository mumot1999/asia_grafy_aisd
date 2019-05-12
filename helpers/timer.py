import time
import statistics


class Timer(object):

    def __init__(self):
        self.measurements = []
        self.mode = 0
        self.last_time = None

    def start(self):
        self.mode = 1
        self.last_time = time.time()

    def stop(self):
        if self.mode == 1:
            self.measurements.append((time.time()-self.last_time))
        self.mode = 0

    def get_mean_time(self):
        return statistics.mean(self.measurements)
