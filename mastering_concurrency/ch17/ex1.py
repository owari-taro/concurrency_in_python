import threading
import sys
sys.setswitchinterval(.000001)
import time

def foo():
    global n
    n+=1

if __name__ == "__main__":
    n = 0
    threads = []
    for i in range(1000):
        thread = threading.Thread(target=foo)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Final value: {n}.')

    print('Finished.')
