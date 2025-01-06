from tkinter import *
from Informes import mostrar_pantalla_informes  # Importa la función para mostrar los informes

class VentanaMonitorRiego:
    def __init__(self, master):
        self.master = master
        self.master.title("Monitor de Riego")
        self.master.geometry("600x450")

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

        # Valores de los estados
        Label(self.miframe, text="Activo", font=("Comic Sans MS", 16)).place(x=440, y=160)
        Label(self.miframe, text="Bajo", font=("Comic Sans MS", 16)).place(x=440, y=200)
        Label(self.miframe, text="Ok", font=("Comic Sans MS", 16)).place(x=440, y=240)
        Label(self.miframe, text="Alta", font=("Comic Sans MS", 16)).place(x=440, y=280)

        Label(self.miframe, text="100%", font=("Comic Sans MS", 16)).place(x=360, y=160)
        Label(self.miframe, text="15%", font=("Comic Sans MS", 16)).place(x=360, y=200)
        Label(self.miframe, text="25%", font=("Comic Sans MS", 16)).place(x=360, y=240)
        Label(self.miframe, text="24°C", font=("Comic Sans MS", 16)).place(x=360, y=280)

        # Botones
        Button(self.miframe, text="Modo Manual", font=("Comic Sans MS", 16), width=10, bg="blue",
               command=self.modo_manual).place(x=20, y=340)
        Button(self.miframe, text="Stop", font=("Comic Sans MS", 16), width=10, bg="red",
               command=self.detener).place(x=160, y=340)
        Button(self.miframe, text="Alarmas", font=("Comic Sans MS", 16), width=10, bg="orange",
               command=self.alarmas).place(x=300, y=340)
        Button(self.miframe, text="Informes", font=("Comic Sans MS", 16), width=10, bg="green",
               command=self.abrir_informes).place(x=440, y=340)

    # Métodos para manejar eventos
    def modo_manual(self):
        print("Cambiando a modo manual")
        # Aquí puedes implementar la lógica correspondiente

    def detener(self):
        print("Deteniendo el sistema de riego")
        self.master.destroy()
        # Aquí puedes implementar la lógica correspondiente

    def alarmas(self):
        print("Mostrando alarmas")
        # Aquí puedes implementar la lógica correspondiente

    def abrir_informes(self):
        from tkinter import messagebox
        messagebox.showinfo("Informes", "Abriendo informes...")
        self.master.destroy()  # Cierra la ventana actual
        mostrar_pantalla_informes()  # Llama a la función para mostrar los informes
    

def mostrar_pantalla_monitor_riego():
    root = Tk()
    app = VentanaMonitorRiego(root)
    root.mainloop()