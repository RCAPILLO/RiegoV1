from tkinter import *
from tkinter import ttk
from MonitorRiego import mostrar_pantalla_monitor_riego  

class VentanaProgramarRiego:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Riego v.1")
        self.master.geometry("500x400")

        self.miframe = Frame(self.master, width=500, height=400)
        self.miframe.pack()

        # Etiquetas de título
        Label(self.miframe, text="Sistema de Riego", font=("Comic Sans MS", 24)).place(x=120, y=20)
        Label(self.miframe, text="Panel de configuración del riego", font=("Comic Sans MS", 18)).place(x=80, y=100)

        # Combobox para seleccionar cultivo
        Label(self.miframe, text="Seleccione cultivo:", font=("Comic Sans MS", 18)).place(x=20, y=180)
        self.cultivo = ttk.Combobox(self.miframe, state="readonly", 
                                    values=["Pimiento", "Tomate", "Maíz"], 
                                    font=("Comic Sans MS", 16), width=12)
        self.cultivo.place(x=240, y=180)

        # Botones
        Button(self.miframe, text="Guardar", width=12,height=1,font=("Comic Sans MS", 16), bg="lightblue",
               command=self.guardar).place(x=70, y=300)
        Button(self.miframe, text="Salir",width=12,height=1, font=("Comic Sans MS", 16), bg="lightblue",
               command=self.master.quit).place(x=250, y=300)

    def guardar(self):
        from tkinter import messagebox
        cultivo = self.cultivo.get()
        if cultivo:
            messagebox.showinfo("Guardado", f"Se configuró el riego para: {cultivo}")
            self.master.destroy()  # Cierra la ventana actual
            mostrar_pantalla_monitor_riego() 
        else:
            messagebox.showwarning("Advertencia", "Debe seleccionar un cultivo.")
def mostrar_pantalla_programar_riego():
    root = Tk()
    app = VentanaProgramarRiego(root)
    root.mainloop()