import threading

saldo = 100
lock = threading.Lock()

def retirar():
    global saldo
    for _ in range(1000):
        lock.acquire()
        saldo = saldo - 1
        lock.release()


hilo1 = threading.Thread(target=retirar)
hilo2 = threading.Thread(target=retirar)

hilo1.start()
hilo2.start()  

hilo1.join()
hilo2.join()   

print(saldo)