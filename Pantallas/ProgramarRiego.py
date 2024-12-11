from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("500x400")
miframe=Frame()
miframe.config(width=500,height=400)
miframe.pack()
EstadoDelSistema=StringVar()
EstadoDelSistema.set("Estado del Sistema")

# Etiquetas de título 
Label(miframe, text="Sistema de Riego", font=("Comic Sans MS", 24), justify="center").place(x=120, y=20)
# Línea horizontal decorativa
Frame(miframe, bg="black", height=2, width=460).place(x=20, y=80)

Label(miframe,text="Panel de configuracion del riego",font=("comic san MS",18)).place(x=80,y=100)
Label(miframe,text="Seleccione cultivo:",font=("comic san MS",18)).place(x=20,y=180)
ElegirCultivo=ttk.Combobox(miframe,state="readonly",values=["Pimiento","Tomate","Maiz"],font=("Comic san MS",18),width=12).place(x=240,y=180)

Guardar=Button(miframe,text="Guardar", font=("Comic san MS",18),width=10,)
Guardar.place(x=80,y=320)
Salir=Button(miframe,text="Salir", font=("Comic san MS",18), width=10)
Salir.place(x=280,y=320)

root.mainloop()