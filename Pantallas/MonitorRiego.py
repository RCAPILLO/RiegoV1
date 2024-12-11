from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("600x450")
miframe=Frame()
miframe.config(width=600,height=450)
miframe.pack()
# Etiquetas de título 
Label(miframe, text="Sistema de Riego", font=("Comic Sans MS", 24), justify="center").place(x=120, y=20)
# Línea horizontal decorativa
Frame(miframe, bg="black", height=2, width=460).place(x=20, y=80)
Label(miframe,text="Monitor de Riego",font=("comic san MS",18)).place(x=80,y=100)

Label(miframe,text="Estado del Sistema", font=("Comic san MS",16)).place(x=20,y=160)
Label(miframe,text="Sensor Humedad zona A",font=("Comic san MS",16)).place(x=20,y=200)
Label(miframe,text="Sensor de HUmedad zona B",font=("Comic san MS",16)).place(x=20,y=240)
Label(miframe,text="Temperatura ambiente",font=("Comic san MS",16)).place(x=20,y=280)

EstadoSistema =Label(text="Activo",font=("Comica San MS",16)).place(x=440,y=160)
EstadoSensorA =Label(text="Bajo",font=("Comica San MS",16)).place(x=440,y=200)
EstadoSensorB =Label(text="Ok",font=("Comica San MS",16)).place(x=440,y=240)
EstadoTemperatura =Label(text="Alta",font=("Comica San MS",16)).place(x=440,y=280)

ValorSistema =Label(text="100%",font=("Comica San MS",16)).place(x=360,y=160)
ValorSensorA =Label(text="15%",font=("Comica San MS",16)).place(x=360,y=200)
ValorSensorB =Label(text="25%",font=("Comica San MS",16)).place(x=360,y=240)
ValorTemperatura =Label(text="24°C",font=("Comica San MS",16)).place(x=360,y=280)


ModoManual=Button(miframe,text="ModoManual",font=("Comic san MS",16),width=10,bg="blue").place(x=20,y=340)
Detener=Button(miframe,text="Stop",font=("Comic san MS",16),width=10,bg="red").place(x=160,y=340)
Alarmas=Button(miframe,text="Alarmas",font=("Comic san MS",16),width=10,bg="orange").place(x=300,y=340)
Informes=Button(miframe,text="Informes",font=("Comic san MS",16),width=10,bg="green").place(x=440,y=340)

root.mainloop()