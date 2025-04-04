import queue
import threading
import time
from datetime import datetime

class RedNeuronal:
    def __init__(self, comunicacion, riego, datos_cola):
        self.comunicacion = comunicacion  # Objeto de la clase Comunicacion
        self.riego = riego  # Objeto de la clase Riego
        self.datos_cola = datos_cola  # Cola para recibir datos entre hilos
        self.hilo_riego = None  # Hilo para ejecutar el riego
        self.ejecutando = threading.Event()  # Control del hilo
        
        # Pesos de la red neuronal (ajustar según entrenamiento)
        self.w_humedad = 0.68
        self.w_temperatura = 0.5
        self.bias = -0.6

    def evaluar_riego(self, humedad_suelo, temp_amb):
        """ Evalúa si se debe activar el riego usando la red neuronal """
        salida_nn = (humedad_suelo * self.w_humedad) + (temp_amb * self.w_temperatura) + self.bias
        return salida_nn > 0  # Si la salida es mayor a 0, activar riego

    def iniciar_riego(self):
        if self.datos_cola.empty():
            print("La cola de datos está vacía. Verifica la conexión con Arduino.")

        """ Inicia el riego en un hilo separado y lo monitorea """
        if self.hilo_riego is None or not self.hilo_riego.is_alive():
            self.ejecutando.set()
            self.hilo_riego = threading.Thread(target=self.regar)
            self.hilo_riego.start()

    def detener_riego(self):
        """ Detiene el riego """
        self.ejecutando.clear()
        self.comunicacion.enviar_datos("OFF")  # Enviar comando a Arduino
        print("Riego detenido")

    def regar(self):
        """ Mantiene el riego activado hasta que la humedad alcance el umbral o pase el tiempo límite """
        inicio = datetime.now()
        self.comunicacion.enviar_datos("ON")
        print("Riego activado")

        while self.ejecutando.is_set():
            try:
                # Leer los datos de la cola
                datos_sensores = self.datos_cola.get(timeout=1)  # Espera hasta 1 segundo para recibir datos
                humedad_suelo, temp_amb, _ = map(float, datos_sensores.split(","))

                if humedad_suelo >= 55 or (datetime.now() - inicio).seconds >= 2400:
                    self.detener_riego()
                    break

                time.sleep(10)  # Revisar cada 10 segundos

            except queue.Empty:
                print("Esperando datos de sensores...")

        # Guardar datos en MySQL
        fin = datetime.now()
        duracion = (fin - inicio).seconds
        self.riego.guardar_en_riego(inicio, fin, humedad_suelo, humedad_suelo, duracion)
