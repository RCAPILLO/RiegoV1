from tkinter import *
global estado
root=Tk()
root.geometry("500x400")

miframe=Frame()
miframe.config(width=500,height=400)
miframe.config(bg="red")
miframe.pack()

labelTitulo=Label(miframe,text="Sistema de Riego",font=("Comic Sans SM",24))
labelTitulo.grid(row=1,column=0)

labelEstadoSistema =Label(miframe,text="Estado del Sistema:")
labelEstadoSistema.grid(row=2,column=0)
labelValorEstadoSistema=Label(miframe,text="Activo")
labelValorEstadoSistema.grid(row=2,column=2)

mainloop()