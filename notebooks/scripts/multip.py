import multiprocessing
from multiprocessing import Process, Pipe, Queue
import time


def standalone_headless(pq, cq, plock):

    plock.acquire()
    print("Lata")
    plock.release()

    time.sleep(0.1)

    msg = pq.get()

    print(msg)
    if msg == 'hello':
        cq.put('gottem1')
        cq.put('gottem2')
        cq.put('gottem3')
    return


if __name__ == "__main__":
    print("Name is indeed main lol")
    plock = multiprocessing.Lock()
    pq, cq = Queue(1), Queue(2)
    p = Process(target=standalone_headless, args=(pq, cq, plock))
    p.daemon = True
    p.start()
    pq.put("hello")
    p.join()
    msg = cq.get()
    print("The message is {}".format(msg))
