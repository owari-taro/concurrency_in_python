import queue
import threading
from enum import Enum


class Task(Enum):
    READER = "reader"
    WRITER = "writer"


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        process_queue()


def process_queue():
    global rcount
    global text

    while not my_queue.empty():
        task = my_queue.get(block=False)
        if task is Task.READER:
            with rcounter:
                rcount += 1
                if rcount == 1:
                    resource.acquire()

            print(
                f'{rcount=}:Reading being done by {threading.current_thread().name}:')
            print(text)
            with rcounter:
                rcount -= 1
                if rcount == 0:
                    resource.release()
        elif task is Task.WRITER:
            with resource:
                tmp = f"writing being done by {threading.current_thread().name}"
                print(tmp)
                text += tmp


if __name__ == "__main__":
    print("test")
    text = "this is some text!"
    my_queue = queue.Queue()
    rcount=0
    tmp = [Task.READER, Task.READER, Task.WRITER,
           Task.READER, Task.WRITER, Task.READER]
    for ele in tmp:
        my_queue.put(ele)
    count = 0
    rcounter = threading.Lock()
    resource = threading.Lock()
    service = threading.Lock()
    threads = [MyThread() for i in range(5)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("hoge")