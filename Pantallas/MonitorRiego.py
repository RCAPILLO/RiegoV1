import queue
from tkinter import *
from .Informes import mostrar_pantalla_informes  # Importa la función para mostrar los informes
from .Comunicacion import Comunicacion
import collections

class VentanaMonitorRiego():
    def __init__(self,master,*args):
        self.master = master
        self.after_id = None  # Asegura que la variable exista desde el inicio
        self.master.title("Monitor de Riego")
        self.master.geometry("600x450")
        self.datos_cola = queue.Queue()
        self.datos_arduino =Comunicacion(self.datos_cola)
        self.datos_recibidos = self.datos_arduino.datos_recibidos  # Usar la misma variable
        self.miframe = Frame(self.master, width=600, height=450)
        self.miframe.pack()

        # Etiquetas de título
        Label(self.miframe, text="Sistema de Riego", font=("Comic Sans MS", 24)).place(x=120, y=20)
        Frame(self.miframe, bg="black", height=2, width=460).place(x=20, y=80)  # Línea horizontal decorativa
        Label(self.miframe, text="Monitor de Riego", font=("Comic Sans MS", 18)).place(x=80, y=100)

        # Estados del sistema
        Label(self.miframe, text="Estado del Sistema", font=("Comic Sans MS", 16)).place(x=20, y=160)
        Label(self.miframe, text="Sensor Humedad zona A", font=("Comic Sans MS", 16)).place(x=20, y=200)
        Label(self.miframe, text="Sensor Humedad zona B", font=("Comic Sans MS", 16)).place(x=20, y=240)
        Label(self.miframe, text="Temperatura ambiente", font=("Comic Sans MS", 16)).place(x=20, y=280)

        # Label dinámicos para mostrar valores actualizados
        self.estado_label = Label(self.miframe, text="Activo", font=("Comic Sans MS", 16))
        self.estado_label.place(x=440, y=160)

        self.humedad_a_label = Label(self.miframe, text="...", font=("Comic Sans MS", 16))
        self.humedad_a_label.place(x=360, y=200)

        self.humedad_b_label = Label(self.miframe, text="...", font=("Comic Sans MS", 16))
        self.humedad_b_label.place(x=360, y=240)

        self.temperatura_label = Label(self.miframe, text="...", font=("Comic Sans MS", 16))
        self.temperatura_label.place(x=360, y=280)

        # Botones
        Button(self.miframe, text="Modo Manual", font=("Comic Sans MS", 16), width=10, bg="blue",
               command=self.modo_manual).place(x=20, y=340)
        Button(self.miframe, text="Stop", font=("Comic Sans MS", 16), width=10, bg="red",
               command=self.detener).place(x=160, y=340)
        Button(self.miframe, text="Alarmas", font=("Comic Sans MS", 16), width=10, bg="orange",
               command=self.alarmas).place(x=300, y=340)
        Button(self.miframe, text="Informes", font=("Comic Sans MS", 16), width=10, bg="green",
               command=self.abrir_informes).place(x=440, y=340)
        
        # Estado de conexión
        self.conexion_label = Label(self.miframe, text="Verificando conexión...", font=("Comic Sans MS", 12))
        self.conexion_label.place(x=20, y=400)
        
       
        
         # Inicializar la comunicación
        self.puertos = self.datos_arduino.puertos_disponibles()
        self.datos_arduino.conexion_serial
        if self.puertos:
            self.datos_arduino.arduino.port = self.puertos[0]
            self.datos_arduino.arduino.baudrate = 9600
            self.datos_arduino.conexion_serial()
            if  self.datos_arduino.arduino and self.datos_arduino.arduino.is_open:
                self.conexion_label.config(text="Conectado a Arduino", fg="green")
            else:
                self.conexion_label.config(text="Error al conectar", fg="red")
        else:
            self.conexion_label.config(text="No hay puertos disponibles", fg="red")
        
        # Iniciar actualización automática
        self.actualizar_datos()

    # Métodos para manejar eventos
    def modo_manual(self):
        print("Cambiando a modo manual")
        """ Método para detener completamente el riego desde Monitor de Riego """
        print("Deteniendo todo el sistema de riego...")
    
        # Asegurarse de que la red neuronal se detenga
        if hasattr(self, 'red_neuronal'):
            self.red_neuronal.detener_riego()
        
        # También detenemos la comunicación con Arduino
        self.datos_arduino.desconectar()
        self.datos_arduino.detener_hilo()
        
        print("Riego detenido con éxito.")
        
    def detener(self):
        print("Deteniendo el sistema de riego")

        # Cancela la actualización automática antes de cerrar
        if hasattr(self, "after_id"):
            self.master.after_cancel(self.after_id)

        self.datos_arduino.desconectar()
        self.datos_arduino.detener_hilo()
    
        self.master.destroy()
        
        from .ProgramarRiego import mostrar_pantalla_programar_riego
        mostrar_pantalla_programar_riego()

    def alarmas(self):
        print("Mostrando alarmas")
        # Aquí puedes implementar la lógica correspondiente
        

    def abrir_informes(self):
        from tkinter import messagebox
        messagebox.showinfo("Informes", "Abriendo informes...")
        self.master.destroy()  # Cierra la ventana actual
        self.datos_arduino.desconectar()
        self.datos_arduino.detener_hilo()
        mostrar_pantalla_informes()  # Llama a la función para mostrar los informes
    
    def actualizar_datos(self):
        # Obtener datos del StringVar
        try:
            # Usamos el método get() del StringVar para obtener el valor actual
            datos_str = self.datos_recibidos.get()
            # Depuración
            print(f"Datos leídos: {datos_str}")
            
            # Verificamos que haya datos
            if datos_str and datos_str.strip():
                # Dividimos los datos usando la coma como separador
                datos = datos_str.split(",")
                
                # Verificamos que tengamos al menos 3 valores
                if len(datos) >= 3:
                    try:
                        # Convertimos a float los valores
                        temperatura = float(datos[0])
                        humedadA = float(datos[1])
                        humedadB = float(datos[2])
                        
                        # Actualizamos las etiquetas con los datos
                        self.temperatura_label.config(text=f"{temperatura} °C")
                        self.humedad_a_label.config(text=f"{humedadA} %")
                        self.humedad_b_label.config(text=f"{humedadB} %")
                        
                        # Actualizamos el estado según la humedad
                        if humedadA > 35:
                            self.estado_label.config(text="Activo", fg="green")
                        else:
                            self.estado_label.config(text="Bajo", fg="red")
                        
                    except (ValueError, IndexError) as e:
                        print(f"Error al procesar datos: {e}")
                else:
                    print(f"Formato de datos incorrecto: {datos}")
            else:
                print("No hay datos disponibles")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        # Programar la próxima actualización en 1 segundo
        self.after_id = self.master.after(1000, self.actualizar_datos)


def mostrar_pantalla_monitor_riego():
    root = Tk()
    # Pasamos comunicacion a Monitor
    monitor = VentanaMonitorRiego(root)  
    root.mainloop()