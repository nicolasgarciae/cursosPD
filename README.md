# Sistema de Reservas Concurrente

## Descripción del proyecto

Este proyecto simula un **sistema de reservas de cursos** donde múltiples usuarios intentan reservar cupos al mismo tiempo.

El objetivo es demostrar los problemas de **concurrencia** cuando varios hilos acceden a un mismo recurso compartido y cómo solucionarlos utilizando mecanismos de sincronización como **Lock** y **Semáforo**.

La simulación considera:

* **50 usuarios intentando reservar**
* **10 cupos disponibles**
* Uso de **hilos (threads)** para simular concurrencia.

---

# Problema

Cuando múltiples hilos acceden a una **variable compartida** (en este caso `cupos`), pueden ocurrir **condiciones de carrera (race condition)**.

Esto significa que varios hilos pueden leer y modificar el valor al mismo tiempo, generando resultados incorrectos como:

* Reservas duplicadas
* Cupos negativos
* Inconsistencia en los datos

---

# Parte 1: Implementación sin Lock

En esta versión no se usa ningún mecanismo de sincronización.

### Funcionamiento

* Se crean **dos hilos**.
* Cada hilo intenta reservar cupos en un ciclo.
* Ambos modifican la variable global `cupos`.

### Código

```python
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
```

### Problema observado

Debido a la ejecución simultánea de los hilos:

* Dos hilos pueden leer el mismo valor de `cupos`.
* Ambos pueden disminuirlo al mismo tiempo.
* Esto genera **inconsistencia en el resultado final**.

Este problema se conoce como **Race Condition**.

---

# Parte 2: Implementación con Lock

Para solucionar el problema anterior se utiliza un **Lock**, que permite que **solo un hilo acceda al recurso compartido a la vez**.

### Funcionamiento

* Se crea un objeto `Lock`.
* Cada hilo debe adquirir el lock antes de modificar `cupos`.
* Los demás hilos deben esperar hasta que el lock se libere.

### Código

```python
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
```

### Resultado

El **Lock evita que dos hilos modifiquen la variable al mismo tiempo**, garantizando que:

* No haya reservas duplicadas
* El número de cupos sea consistente
* El valor final sea correcto

---

# Parte 3: Implementación con Semáforo

En esta versión se usa un **Semáforo**, que permite controlar cuántos hilos pueden acceder al recurso simultáneamente.

### Ejemplo del proyecto

El semáforo permite **2 reservas simultáneas**.

### Código

```python
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
```

### Funcionamiento

* El semáforo controla cuántos hilos pueden entrar al mismo tiempo.
* En este caso, **máximo 2 usuarios pueden reservar simultáneamente**.
* Los demás hilos deben esperar hasta que el semáforo libere un espacio.

---

# Comparación de resultados

| Método       | Comportamiento                                            |
| ------------ | --------------------------------------------------------- |
| Sin Lock     | Puede producir inconsistencias y condiciones de carrera   |
| Con Lock     | Garantiza acceso exclusivo al recurso compartido          |
| Con Semáforo | Permite acceso controlado de varios hilos simultáneamente |

---

# Conclusiones

* Los sistemas concurrentes pueden generar **problemas de sincronización** si varios hilos acceden al mismo recurso.
* **Lock** es útil cuando se necesita **exclusión mutua total**.
* **Semáforos** permiten **controlar el número de accesos concurrentes**.
* Estos mecanismos son fundamentales en sistemas reales como:

  * Sistemas de reservas
  * Bases de datos
  * Sistemas distribuidos
  * Servidores web

---

# Cómo ejecutar el proyecto

1. Clonar el repositorio

```bash
git clone https://github.com/nicolasgarciae/cursosPD
```

2. Ejecutar cualquiera de los archivos

```bash
python3 cuposSL.py
python3 cursos.py
python3 cursosSEM.py
```

---

# Autor

Proyecto académico de **concurrencia en Python** utilizando la librería `threading`.
