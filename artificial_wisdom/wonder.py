import functools
import time



class Wonder:
    def __init__(self, function):
        functools.update_wrapper(self, function)
        self.function = function
        self.running_times = []

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        value = self.function(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        running_time = {
            "timestamp": time.time(),
            "run_time": run_time,
        }
        self.running_times.append(running_time);
        return value
