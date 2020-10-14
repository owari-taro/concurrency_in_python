import threading
import time
# The philosopher thread


def philosopher(left, right, no):
    while True:
        with left:
            print(f"no{no}:catch left")
            with right:
                print(f"no{no}:tach right")
                print(
                    f'{time.time()}:Philosopher at {threading.currentThread()} is eating.')


# The chopsticks
N_FORKS = 5
# each forks is represented by lock object
forks = [threading.Lock() for n in range(N_FORKS)]

# Create all of the philosophers
phils = [threading.Thread(
    target=philosopher,
    args=(forks[n], forks[(n + 1) % N_FORKS],n)
) for n in range(N_FORKS)]

# Run all of the philosophers
for p in phils:
    p.start()
