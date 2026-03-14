import threading

lock = threading.Lock()
asientos = 10

def reservar():
    global asientos
    
    with lock:
        if asientos > 0:
            asientos -= 1
            print("Asiento reservado, quedan", asientos)
        else:
            print("No quedan asientos disponibles")

for i in range(50):
    threading.Thread(target=reservar).start()