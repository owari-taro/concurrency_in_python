import requests

def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.status_code}')




if __name__=="__main__":
    import time
    urls = [
        'http://httpstat.us/200',
        'http://httpstat.us/400',
        'http://httpstat.us/404',
        'http://httpstat.us/408',
        'http://httpstat.us/500',
        'http://httpstat.us/524'
    ]
    st=time.time()
    for url in urls:
        ping(url)

    print('Done.')
    print(time.time()-st)