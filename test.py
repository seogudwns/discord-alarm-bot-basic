import threading
import time

def myfunc(a,b):
    for i in range(a,b):
        print(i)
    return

def myfunc2(n):
    print(n)
    return

print(time.time())
threading.Timer(interval=1, function=myfunc,args=(1,6)).start()
threading.Timer(interval=2, function=myfunc2,kwargs='qwer')
print(time.time())


