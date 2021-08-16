import time
start = time.perf_counter()
def func():
    print('durmiendo1')
    time.sleep(1)
    print("terminado1")

def func1():
    print('durmiendo2')
    time.sleep(1)
    print("terminado2")
func()
func1()

finish = time.perf_counter()
print(f'Terminado en {round(finish-start, 2)} segundo(s)')