import threading
import time

sem = threading.Semaphore(2)
cupos = 10
def reservar(nombre):
    global cupos
    sem.acquire()
    if cupos > 0:
        cupos -= 1  
        print(nombre, "está reservando...")
        time.sleep(2)
        print(nombre, "termino")
    sem.release()

for i in range(50):

    threading.Thread(
        target=reservar, 
        args=(f"Usuario {i}",)
    ).start()