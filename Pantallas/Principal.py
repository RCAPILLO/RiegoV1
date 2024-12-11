from tkinter import *
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

Label(miframe,text="Estado del sistema",font=("Comic san MS",18)).place(x=20,y=100)
EstadoSistema=Label(text="Inactivo",font=("comic san ms",18)).place(x=320,y=100)
Label(miframe,text="Temperatura",font=("Comic san MS",18)).place(x=20,y=140)
EstadoSistema=Label(text="18°C",font=("comic san ms",18)).place(x=320,y=140)
Label(miframe,text="Humedad del Campo",font=("Comic san MS",18)).place(x=20,y=180)
EstadoSistema=Label(text="25%",font=("comic san ms",18)).place(x=320,y=180)

#Boton para iniciar el riego o colocarlo activo
start=Button(miframe,text="Iniciar Riego",font=("comic san MS",18))
start.place(x=120,y=280)

root.mainloop()