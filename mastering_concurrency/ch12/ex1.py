import threading
import time


def thread_a():
    print('Thread A is starting...')

    print('Thread A waiting to acquire lock A.')
    lock_a.acquire()
    print('Thread A has acquired lock A, performing some calculation...')
    time.sleep(2)

    print('Thread A waiting to acquire lock B.')
    print("\nactive threads:{}\n".format(threading.active_count()))

    lock_b.acquire()
    print('Thread A has acquired lock B, performing some calculation...')
    time.sleep(2)

    print('Thread A releasing both locks.')
    lock_a.release()
    lock_b.release()


def thread_b():
    print('Thread B is starting...')

    print('Thread B waiting to acquire lock B.')
    lock_b.acquire()
    print('Thread B has acquired lock B, performing some calculation...')
    time.sleep(5)
    print('Thread B waiting to acquire lock A.')
    print("\nactive threads:{}\n".format(threading.active_count()))

    lock_a.acquire()
    print('Thread B has acquired lock A, performing some calculation...')
    time.sleep(5)

    print('Thread B releasing both locks.')
    lock_b.release()
    lock_a.release()


if __name__ == "__main__":
    lock_a = threading.Lock()
    lock_b = threading.Lock()

    thread1 = threading.Thread(target=thread_a)
    thread2 = threading.Thread(target=thread_b)
    print("\nactive threads:{}\n".format(threading.active_count()))

    thread1.start()
    print("\nactive threads:{}\n".format(threading.active_count()))
    thread2.start()
    
    thread1.join()
    thread2.join()

    print('Finished.')
