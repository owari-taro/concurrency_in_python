import threading
import time
# The philosopher thread


def philosopher(left, right, n):
    while True:
        print(f"waiting left :{n} {id(left)}")
        with left:
            print(f"waiting right :{n} {id(right)}")
            with right:
                print(
                    f"{time.time()} philosopher at {threading.currentThread()} is eating")


if __name__ == "__main__":
    # The chopsticks
    N_FORKS = 5
    # each forks is represented by lock object
    forks = [threading.Lock() for n in range(N_FORKS)]

    # Create all of the philosophers
    phils = [threading.Thread(
        target=philosopher,
        args=(forks[n], forks[(n + 1) % N_FORKS], n)
    ) for n in range(N_FORKS)]

    # Run all of the philosophers
    for p in phils:
        p.start()
