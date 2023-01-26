from multiprocessing import Process


def say_hello(name: str) -> str:
    return f"hi there {name}"


import time


def count(to: int) -> int:
    st = time.time()
    counter = 0
    while counter < to:
        counter = counter + 1
    ed = time.time()
    print(f"finished counting to {to} in {ed -st}")


if __name__ == "__main__":
    st = time.time()
    one = Process(target=count, args=(100_000_000,))
    two = Process(target=count, args=(200_000_000,))
    one.start()
    two.start()
    one.join()
    two.join()
    ed = time.time()
    print(f"{ed-st}")
