import threading
import time


def writer():
    global text

    while True:
        with resource:
            time.sleep(1.3)
            print(f'Writing being done by {threading.current_thread().name}.')
            text += f'Writing was done by {threading.current_thread().name}. '


def reader():
    global rcount

    while True:
        with rcounter:
            rcount += 1
            if rcount == 1:
                resource.acquire()

        print(f'{rcount=}:Reading being done by {threading.current_thread().name}:')
        print(text)

        with rcounter:
            rcount -= 1
            if rcount == 0:
                resource.release()


if __name__ == "__main__":
    text = 'This is some text. '
    rcount = 0

    rcounter = threading.Lock()
    resource = threading.Lock()

    threads = [threading.Thread(target=reader) for i in range(
        1)] + [threading.Thread(target=writer) for i in range(2)]

    for thread in threads:
        thread.start()
