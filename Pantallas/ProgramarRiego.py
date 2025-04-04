import gc
from tkinter import *
from tkinter import ttk
from .MonitorRiego import mostrar_pantalla_monitor_riego  
from Clases.Riego import Riego
import sys
import os
from datetime import datetime,date

# Obtener la ruta del directorio raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class VentanaProgramarRiego:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Riego v.1")
        self.master.geometry("500x400")
        self.miframe = Frame(self.master, width=500, height=400)
        self.miframe.pack()
        # 📌 Instanciar conexión con la base de datos
        self.base_datos = Riego(
            host="localhost",
            user="root",
            password="",
            database="sistema_riego"
        )

        # Etiquetas de título
        Label(self.miframe, text="Sistema de Riego", font=("Comic Sans MS", 24)).place(x=120, y=20)
        Label(self.miframe, text="Panel de configuración del riego", font=("Comic Sans MS", 18)).place(x=80, y=100)

        # Combobox para seleccionar cultivo
        Label(self.miframe, text="Seleccione cultivo:", font=("Comic Sans MS", 12)).place(x=20, y=180)
        self.cultivo = ttk.Combobox(self.miframe, state="readonly", 
                                    values=["Pimiento", "Tomate", "Maíz"], 
                                    font=("Comic Sans MS", 12), width=12)
        self.cultivo.place(x=300, y=180)

        Label(self.miframe, text="Seleccione zona:", font=("Comic Sans MS", 12)).place(x=20, y=220)
        self.zona = ttk.Combobox(self.miframe, state="readonly", values=["Norte", "Sur", "Este", "Oeste"], font=("Comic Sans MS", 12), width=12)
        self.zona.place(x=300, y=220)

        Label(self.miframe, text="Fecha de siembra (dd/mm/aaaa):", font=("Comic Sans MS", 12)).place(x=20, y=260)
        self.fecha_siembra = Entry(self.miframe, font=("Comic Sans MS", 12), width=12)
        self.fecha_siembra.place(x=300, y=260)

        # Botones
        self.boton_guardar=Button(self.miframe, text="Guardar", width=12,height=1,font=("Comic Sans MS", 12), bg="lightblue",
               command=self.guardar)
        self.boton_guardar.place(x=30, y=320)
        self.boton_nuevo=Button(self.miframe, text="Nuevo", width=12,height=1,font=("Comic Sans MS", 12), bg="lightblue",
               command=self.nuevo_riego)
        self.boton_nuevo.place(x=130, y=320)

        self.boton_ir_monitor=Button(self.miframe, text="Monitor", width=12,height=1,font=("Comic Sans MS", 12), bg="lightblue",
               command=self.ir_monitor)
        self.boton_ir_monitor.place(x=250, y=320)

        self.boton_salir=Button(self.miframe, text="Atras",width=12,height=1, font=("Comic Sans MS", 12), bg="lightblue",
               command=self.cerrar_pantalla_atras)
        self.boton_salir.place(x=350, y=320)
        
        # Cargar último riego programado
        self.cargar_ultimo_riego()
        self.validar_campos()
        # Asociar evento de validación
        self.cultivo.bind("<<ComboboxSelected>>", self.validar_campos)
        self.zona.bind("<<ComboboxSelected>>", self.validar_campos)
        #self.fecha_siembra.bind("<KeyRelease>",self.validar_campos)

    def guardar(self):
        from tkinter import messagebox
        """ Guarda el cultivo en la base de datos  """
        cultivo = self.cultivo.get()
        zona = self.zona.get()
        fecha_siembra = self.fecha_siembra.get()

        if cultivo and zona and fecha_siembra:
            try:
                fecha_siembra_mysql = self.convertir_fecha_mysql(fecha_siembra)
                self.base_datos.guardar_cultivo(cultivo, zona, fecha_siembra_mysql)
                messagebox.showinfo("Guardado", f"Se guardó el riego para: {cultivo} en {zona} ({fecha_siembra})")

                self.cerrar_pantalla()
                mostrar_pantalla_monitor_riego()
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha incorrecto. Use DD/MM/AAAA.")
        else:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")
    def convertir_fecha_mysql(self, fecha):
        """ Convierte fecha de DD/MM/AAAA a AAAA-MM-DD para MySQL """
        dia, mes, año = fecha.split("/")
        return f"{año}-{mes}-{dia}"
    
    def cerrar_pantalla_atras(self):
        """ Cierra la ventana y libera memoria """
        self.master.destroy()  # Cierra la ventana
        gc.collect()  # Libera memoria en caso lo este usando
        from .Principal import mostrar_pantalla_principal
        mostrar_pantalla_principal()
    
    def cargar_ultimo_riego(self):
        datos = self.base_datos.ultimo_riego_programado()
        if datos:
            tipo_cultivo, zona, fecha_riego = datos
             # Si `fecha_riego` es `datetime.date`, conviértelo a string
            if isinstance(fecha_riego, date):
                fecha_riego_str = fecha_riego.strftime("%d/%m/%Y")
            else:
                fecha_riego_str = datetime.strptime(fecha_riego, "%Y-%m-%d").strftime("%d/%m/%Y")

            self.cultivo.set(tipo_cultivo)
            self.zona.set(zona)
            self.fecha_siembra.delete(0,END)  
            self.fecha_siembra.insert(0, fecha_riego_str)  
        else:
            print("No se encontraron registros previos.")
    def nuevo_riego(self):
            self.cultivo.set("")
            self.zona.set("")
            self.fecha_siembra.delete(0,END)  
            self.fecha_siembra.insert(0, "")  
    def validar_campos(self, event=None):
        """Habilita o deshabilita los botones según el estado de los campos."""
        campos_llenos = all([self.cultivo.get(), self.zona.get(), self.fecha_siembra.get()])

        if campos_llenos:
            self.boton_guardar.config(state=DISABLED)  # Deshabilitar "Guardar"
            self.boton_nuevo.config(state=NORMAL)  # Activar "Nuevo"
        else:
            self.boton_guardar.config(state=NORMAL)  # Activar "Guardar"
            self.boton_nuevo.config(state=DISABLED)  # Deshabilitar "Nuevo"
    def cerrar_pantalla(self):
        """ Cierra la ventana y libera memoria """
        self.master.destroy()  # Cierra la ventana
        gc.collect()  # Libera memoria en caso lo este usando
        
    def ir_monitor(self):
        self.cerrar_pantalla()
        mostrar_pantalla_monitor_riego()  

def mostrar_pantalla_programar_riego():
    root = Tk()
    app = VentanaProgramarRiego(root)
    root.mainloop()