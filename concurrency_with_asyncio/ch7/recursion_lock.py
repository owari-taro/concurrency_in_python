from threading import RLock,Thread
from typing import List
list_lock=RLock()

def sum_list(int_list:list[int])->int:
    with list_lock:
        if len(int_list)==0:
            print("finished summing")
            return 0
        else:
            head,*tail=int_list
            print("summing rest of list")
            return head+sum(tail)


if __name__=="__main__":
    thread=Thread(target=sum_list,args=([1,2,3,4],))
    thread.start()
    thread.join()
    print(thread)