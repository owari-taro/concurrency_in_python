import threading
import random
import time


def update():
    global counter
    print(f"counter={counter},{threading.current_thread().name}")
    current_counter = counter  # reading in shared resource
    time.sleep(random.randint(0, 1))  # simulating heavy calculations
    counter = current_counter + 1  # updating shared resource


if __name__ == "__main__":

    counter = 0
    st=time.time()
    threads = [threading.Thread(target=update) for i in range(20)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    ed=time.time()
    print(f'Final counter: {counter}.')
    print('Finished.')
    print(f"elapsed:{ed-st}")