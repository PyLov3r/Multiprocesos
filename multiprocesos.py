import multiprocessing
import time
start = time.perf_counter()
def do_something():
    print('Durmiendo un segundo...')
    time.sleep(1)
    print('Terminando de dormir...')
p = multiprocessing.Process(target=do_something)
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)
p3 = multiprocessing.Process(target=do_something)   
if __name__ == '__main__':
    p.start()
    p1.start()
    p2.start()
    p3.start()
    p.join()
    p1.join()
    p2.join()
    p3.join()
    finish = time.perf_counter()
    print(f'Terminado en {round(finish-start, 2)} segundo(s)')
   
