
import threading
import time

# Función para hilo 1
def reloj1():
    while True:
        hora_actual = time.strftime("%H:%M:%S")
        print(f"Hilo 1: {hora_actual}")
        time.sleep(1)

# Función para hilo 2
def reloj2():
    while True:
        hora_actual = time.strftime("%H:%M:%S")
        print(f"Hilo 2: {hora_actual}")
        time.sleep(1)

# Crear hilos
hilo1 = threading.Thread(target=reloj1)
hilo2 = threading.Thread(target=reloj2)

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar tiempo antes de interrumpir los hilos
time.sleep(5)

# Interrumpir los hilos
hilo1.join(timeout=0)
hilo2.join(timeout=0)

# Mostrar mensaje cuando los hilos sean interrumpidos
print("Hilos interrumpidos")

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()