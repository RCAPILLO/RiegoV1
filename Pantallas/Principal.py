from tkinter import *
from ProgramarRiego import mostrar_pantalla_programar_riego  # Asegúrate de que el archivo ProgramarRiego.py esté bien referenciado.

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Riego v.1")
        self.master.geometry("500x500")

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
        self.Temperatura = Label(self.miframe, text="18°C", font=("Comic san MS", 18))
        self.Temperatura.place(x=320, y=140)
        Label(self.miframe, text="Humedad del Campo", font=("Comic san MS", 18)).place(x=20, y=180)
        self.HumedadCampo = Label(self.miframe, text="25%", font=("Comic san MS", 18))
        self.HumedadCampo.place(x=320, y=180)

        # Botón para iniciar el riego o colocarlo activo
        self.start = Button(self.miframe, text="Iniciar Riego",width=12,height=1, font=("Comic san MS", 18),
                            command=self.iniciar_riego)
        self.start.place(x=40, y=280)

        self.salirprograma=Button(self.miframe,text="salir",width=12,height=1, font=("Comic san MS",18),
                          command=self.salir)
        self.salirprograma.place(x=290,y=280)

    def iniciar_riego(self):
        """ Método para iniciar el riego y cerrar la ventana actual """
        self.master.destroy()  # Cerrar la ventana actual
        mostrar_pantalla_programar_riego()  # Llamar a la función para programar el riego
    def salir(self):
        self.master.destroy()
# Ejemplo de cómo crear y ejecutar esta ventana principal
def mostrar_pantalla_principal():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()

