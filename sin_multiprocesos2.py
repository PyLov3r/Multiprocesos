
import time
start = time.perf_counter()
x = 900000
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

def do_something(): 
    f= open("archivo.txt","w+")
    for i in range(x):
        f.write("This is line %d\r\n" % (i+1))
    func()
    func1()
    func2()
    func3()

def do_something1():
    f= open("archivo1.txt","w+")
    for i in range(x):
        f.write("This is line %d\r\n" % (i+1)) 
    func()
    func1()
    func2()
    func3()
def do_something2():
    f= open("archivo2.txt","w+")
    for i in range(x):
        f.write("This is line %d\r\n" % (i+1))
    func()
    func1()
    func2()
    func3()
def do_something3():
    f= open("archivo3.txt","w+")
    for i in range(x):
        f.write("This is line %d\r\n" % (i+1))
    func()
    func1()
    func2()
    func3()
do_something()
do_something1()
do_something2()
do_something3()
finish = time.perf_counter()
print(f'Terminado en {round(finish-start, 2)} segundo(s)')