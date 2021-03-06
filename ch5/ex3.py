import threading
import requests
import time


def ping(url):
    res = requests.get(url)
    time.sleep(1)
    print(f'{url}: {res.status_code}')


if __name__ == "__main__":
    urls = [
        'http://httpstat.us/200',
        'http://httpstat.us/400',
        'http://httpstat.us/404',
        'http://httpstat.us/408',
        'http://httpstat.us/500',
        'http://httpstat.us/524'
    ]

    start = time.time()
    for url in urls:
        ping(url)
    print(f'Sequential: {time.time() - start : .2f} seconds')

    print()

    start = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=ping, args=(url,))
        threads.append(thread)
        thread.start()
        #thread.join()

    for thread in threads:
        #wait until each thread is finished
        thread.join()

    print(f'Threading: {time.time() - start : .2f} seconds')
