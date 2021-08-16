import multiprocessing
import threading
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
def func2():
        print('durmiendo3')
        time.sleep(1)
        print("terminado3")
def func3():
        print('durmiendo4')
        time.sleep(1)
        print("terminado4")
x = 900000
def do_something():
    x = 900000
    f= open("archivo.txt","w+")
    for i in range(x):
        f.write("This is line %d\r\n" % (i+1))

    x = threading.Thread(target=func)
    x1 = threading.Thread(target=func1)
    x2 = threading.Thread(target=func2)
    x3 = threading.Thread(target=func3)
    x.start() 
    x1.start() 
    x2.start() 
    x3.start()
    x.join()
    x1.join()
    x2.join()
    x3.join()
def do_something1():
    x = 900000
    f= open("archivo1.txt","w+")
    for i in range(x):
        f.write("This is line %d\r\n" % (i+1)) 
    x = threading.Thread(target=func)
    x1 = threading.Thread(target=func1)
    x2 = threading.Thread(target=func2)
    x3 = threading.Thread(target=func3)
    x.start() 
    x1.start() 
    x2.start() 
    x3.start()
    x.join()
    x1.join()
    x2.join()
    x3.join()
def do_something2():
    x = 900000
    f= open("archivo2.txt","w+")
    for i in range(x):
        f.write("This is line %d\r\n" % (i+1))
    x = threading.Thread(target=func)
    x1 = threading.Thread(target=func1)
    x2 = threading.Thread(target=func2)
    x3 = threading.Thread(target=func3)
    x.start() 
    x1.start() 
    x2.start() 
    x3.start()
    x.join()
    x1.join()
    x2.join()
    x3.join()
def do_something3():
    x = 900000
    f= open("archivo3.txt","w+")
    for i in range(x):
        f.write("This is line %d\r\n" % (i+1))
    x = threading.Thread(target=func)
    x1 = threading.Thread(target=func1)
    x2 = threading.Thread(target=func2)
    x3 = threading.Thread(target=func3)
    x.start() 
    x1.start() 
    x2.start() 
    x3.start()
    x.join()
    x1.join()
    x2.join()
    x3.join()
p = multiprocessing.Process(target=do_something)
p1 = multiprocessing.Process(target=do_something1)
p2 = multiprocessing.Process(target=do_something2)
p3 = multiprocessing.Process(target=do_something3)   
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