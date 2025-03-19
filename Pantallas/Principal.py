from tkinter import *
from .ProgramarRiego import mostrar_pantalla_programar_riego  # Asegúrate de que el archivo ProgramarRiego.py esté bien referenciado.
from .Comunicacion import Comunicacion

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Riego v.1")
        self.master.geometry("500x500")
        self.datos_arduino =Comunicacion()
        self.datos_recibidos = self.datos_arduino.datos_recibidos  # Usar la misma variable

        # Configuración del marco
        self.miframe = Frame(self.master)
        self.miframe.config(width=500, height=500)
        self.miframe.pack()

        # Variable para el estado del sistema
        self.EstadoDelSistema = StringVar()
        self.EstadoDelSistema.set("Estado del Sistema")

        # Etiquetas de título 
        Label(self.miframe, text="Sistema de Riego", font=("Comic Sans MS", 24), justify="center").place(x=120, y=20)
        # Línea horizontal decorativa
        Frame(self.miframe, bg="black", height=2, width=460).place(x=20, y=80)

        # Etiquetas para los estados
        Label(self.miframe, text="Estado del sistema", font=("Comic san MS", 18)).place(x=20, y=100)
        self.EstadoSistema = Label(self.miframe, text="Inactivo", font=("Comic san MS", 18))
        self.EstadoSistema.place(x=320, y=100)
        Label(self.miframe, text="Temperatura", font=("Comic san MS", 18)).place(x=20, y=140)
        self.Temperatura = Label(self.miframe, text="...", font=("Comic san MS", 18))
        self.Temperatura.place(x=320, y=140)
        Label(self.miframe, text="Humedad del Campo", font=("Comic san MS", 18)).place(x=20, y=180)
        self.HumedadCampo = Label(self.miframe, text="...", font=("Comic san MS", 18))
        self.HumedadCampo.place(x=320, y=180)

        # Botón para iniciar el riego o colocarlo activo
        self.start = Button(self.miframe, text="Iniciar Riego",width=12,height=1, font=("Comic san MS", 18),
                            command=self.iniciar_riego)
        self.start.place(x=40, y=280)

        self.salirprograma=Button(self.miframe,text="salir",width=12,height=1, font=("Comic san MS",18),
                          command=self.salir)
        self.salirprograma.place(x=290,y=280)

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
            if self.datos_arduino.arduino.is_open:
                self.conexion_label.config(text="Conectado a Arduino", fg="green")
            else:
                self.conexion_label.config(text="Error al conectar", fg="red")
        else:
            self.conexion_label.config(text="No hay puertos disponibles", fg="red")

        # Iniciar actualización automática
        self.actualizar_datos()

    def iniciar_riego(self):
        """ Método para iniciar el riego y cerrar la ventana actual """
        self.datos_arduino.desconectar()
        self.datos_arduino.detener_hilo()
        self.master.destroy()  # Cerrar la ventana actual
        mostrar_pantalla_programar_riego()  # Llamar a la función para programar el riego
    def salir(self):
        self.master.destroy()

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
                        self.Temperatura.config(text=f"{temperatura} °C")
                        self.HumedadCampo.config(text=f"{humedadB} %")
                        
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
        
# Ejemplo de cómo crear y ejecutar esta ventana principal
def mostrar_pantalla_principal():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()

