
import serial, serial.tools.list_ports
from threading import Thread,Event
from tkinter import StringVar

class Comunicacion:
    def __init__(self,*args):
        super().__init__(*args)
        self.datos_recibidos=StringVar()
        self.arduino=serial.Serial()
        self.arduino.timeout=2
        self.braudates=['1200','2400','4800','9600','19200','38400','115200']
        self.puertos=[]
        self.señal=Event()
        self.hilo=None

    def puertos_disponibles(self):
        self.puertos=[port.device for port in serial.tools.list_ports.comports()]
    
    def conexion_serial(self):
        try:
            self.arduino.open()
        except:
            pass
        if (self.arduino.is_open):
            self.iniciar_hilo()
            print('Conectado arduino')
        
    def enviar_datos(self, data):
        if (self.arduino.is_open):
            self.datos=str(data)+"\n"
            self.arduino.write(self.datos.encode())
        else:
            print('Error an enviar datos')

    def leer_datos(self):
        try:
            while(self.señal.isSet()and self.arduino.is_open ):
                data=self.arduino.readline().decode('utf-8').strip()
                if not data:  # Evita procesar líneas vacías
                    continue  
                print("Datos recibidos:", data)  # Verifica qué llega exactamente
                self.datos_recibidos.set(data)  # Guarda los datos
                print(f'Datos guardados',self.datos_recibidos)
        except (UnicodeDecodeError, TypeError) as e:
            print(f"Error al leer datos: {e}")  
            # Manejar errores específicos
        except Exception as e:
            print(f"Error inesperado: {e}")  
            # Capturar cualquier otro error

    def iniciar_hilo(self):
        self.hilo=Thread(target=self.leer_datos)
        self.hilo.setDaemon(1)
        self.señal.set()
        self.hilo.start()

    def detener_hilo(self):
        if(self.hilo is not None):
            self.señal.clear()
            self.hilo.join()
            self.hilo=None

    def desconectar(self):
        self.arduino.close()
        self.detener_hilo()
    


