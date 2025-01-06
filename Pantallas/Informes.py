from tkinter import *
from MostrarGrafico import mostrarGrafico  # Importa la función para mostrar gráficos

class VentanaInformes:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Riego")
        self.master.geometry("600x500")

        # Crear el marco
        self.miframe = Frame(self.master, width=600, height=500)
        self.miframe.pack()

        # Etiqueta de título
        Label(self.miframe, text="Sistema de Riego", font=("Comic Sans MS", 24)).place(x=20, y=20)
        Frame(self.miframe, bg="black", height=2, width=460).place(x=20, y=80)  # Línea decorativa

        # Botón para ver el informe
        Button(self.miframe, text="Ver Informe",width=12,height=1, font=("Comic Sans MS", 14), bg="blue", fg="white",
               command=self.mostrar_grafico).place(x=100, y=200)
        Button(self.miframe, text="Volver", width=12,height=1,font=("Comic Sans MS", 14), bg="green", fg="white",
               command=self.volver_a_monitor).place(x=100, y=150)

    # Método para mostrar el gráfico
    def mostrar_grafico(self):
        mostrarGrafico()  # Llama a la función `mostrarGrafico`
    def volver_a_monitor(self):
        from MonitorRiego import mostrar_pantalla_monitor_riego
        self.master.destroy()  # Cierra la ventana actual
        mostrar_pantalla_monitor_riego()
        

def mostrar_pantalla_informes():
    root = Tk()
    app = VentanaInformes(root)
    root.mainloop()