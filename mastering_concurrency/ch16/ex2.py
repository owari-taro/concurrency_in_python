import threading
import time


class LockedCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self, x):
        with self.lock:
            new_value = self.value+x
            time.sleep(0.01)
            self.value = new_value

    def get_value(self):
        with self.lock:
            value = self.value
        return value


class LockedCounter2:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    # make increment function faster by putting sleep-funcion outside with-block

    def increment(self, x):
        time.sleep(0.01)
        with self.lock:
            new_value = self.value+x
            self.value = new_value

    def get_value(self):
        with self.lock:
            value = self.value
        return value


if __name__ == "__main__":
    st = time.time()
    from concurrent.futures import ThreadPoolExecutor
    counter = LockedCounter()
    with ThreadPoolExecutor(max_workers=3)as executor:
        executor.map(counter.increment, [1 for i in range(300)])
    print(f"final counter {counter.get_value()}")
    ed = time.time()
    print("finsihed")
    print(f"elapsed:{ed-st}")
    print("####################################################\n\n")
    counter = LockedCounter2()
    st = time.time()
    with ThreadPoolExecutor(max_workers=3)as executor:
        executor.map(counter.increment, [1 for i in range(300)])
    print(f"final counter {counter.get_value()}")
    ed = time.time()
    print("finsihed")
    print(f"elapsed:{ed-st}")
