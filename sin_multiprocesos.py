import time

start = time.perf_counter()

def do_something():
    print('Durmiendo un segundo...')
    time.sleep(1)
    print('Terminando de dormir...')

    
do_something()
do_something()
do_something()
do_something()

finish = time.perf_counter()

print(f'Terminado en {round(finish-start, 2)} segundo(s)')