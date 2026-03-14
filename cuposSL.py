import threading

cupos = 10

def reservar():
    global cupos
    
    for i in range(50):
        if cupos > 0:
            cupos = cupos - 1
            print("Cupo reservado, quedan", cupos)
        else:
            print("No quedan cupos disponibles")

hilo1 = threading.Thread(target=reservar)
hilo2 = threading.Thread(target=reservar)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Cupos finales:", cupos)