import threading
import time

sem = threading.Semaphore(2)

def imprimir(nombre):

    sem.acquire()

    print(nombre, "está imprimiendo...")
    time.sleep(2)
    print(nombre, "termino")
    sem.release()

for i in range(5):

    threading.Thread(
        target=imprimir, 
        args=(f"Usuario {i}",)
    ).start()