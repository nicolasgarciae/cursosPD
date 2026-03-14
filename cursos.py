import threading

lock = threading.Lock()
cupos = 10

def reservar():
    global cupos
    
    with lock:
        if cupos > 0:
            cupos -= 1
            print("Cupo reservado, quedan", cupos)
        else:
            print("No quedan cupos disponibles")

for i in range(50):
    threading.Thread(target=reservar).start()