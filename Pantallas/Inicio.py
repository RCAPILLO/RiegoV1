from tkinter import *
import mysql.connector

# Conexión a la base de datos MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",       # Servidor local
        user="root",            # Usuario de MySQL 
        password="",            # Contraseña de MySQL 
        database="riego"        # Nombre de la base de datos
    )

# Función para validar usuario y contraseña desde la base de datos
def validar_usuario():
    usuario_input = usuario.get()
    pasword_input = pasword.get()

    try:
        conn = conectar_bd()
        cursor = conn.cursor()

        # Consulta para verificar usuario y contraseña
        cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND password = %s", 
                       (usuario_input, pasword_input))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            # Si las credenciales son correctas, abrir nueva ventana
            print("Bien venido al sistema de riego v1")
        else:
            mensaje_error["text"] = "Usuario o contraseña incorrectos"
    except mysql.connector.Error as err:
        mensaje_error["text"] = f"Error de conexión: {err}"


# Función para manejar el evento de "Olvidé mi contraseña"
def recuperar_contraseña(event):
    # Mostrar un mensaje en consola por ahora (puedes agregar más lógica aquí)
    print("Redirigir a la página de recuperación de contraseña")

# Configuración de la ventana principal
root = Tk()
root.title("Sistema de riego V.1")
root.geometry("500x400")
root.iconbitmap("Imagenes/LogoRiegoV1.ico")
root.resizable(0,0)
# Configuración del marco
miframe = Frame(root, width=500, height=400)
miframe.pack()

# Etiquetas de título 
Label(miframe, text="Sistema de Riego", font=("Comic Sans MS", 24), justify="center").place(x=120, y=20)
# Línea horizontal decorativa
Frame(miframe, bg="black", height=2, width=460).place(x=20, y=80)
# Etiquetas de casillas para iniciar sesion
Label(miframe, text="Usuario", font=("Comic Sans MS", 16)).place(x=20, y=120)
Label(miframe, text="Password", font=("Comic Sans MS", 16)).place(x=20, y=180)

# Campos de entrada
usuario = Entry(miframe, font=("Arial", 14))
usuario.place(x=140, y=120, width=200)
pasword = Entry(miframe, font=("Arial", 14), show="*")
pasword.place(x=140, y=180, width=200)

# Mensaje de error inicializado como un Label vacío
mensaje_error = Label(miframe, text="", font=("Arial", 12), fg="red")
mensaje_error.place(x=140, y=220)  # Posiciona el mensaje de error en la pantalla

# Botón de inicio
iniciar = Button(miframe, text="Iniciar Sesión", font=("Arial", 14), bg="lightblue",command=validar_usuario,cursor="hand2")
iniciar.place(x=180, y=250)

# Mensaje "Olvidé mi contraseña" (con evento de clic)
mensaje_olvide = Label(miframe, text="Olvidé mi contraseña", font=("Arial", 12), fg="blue", cursor="hand2")
mensaje_olvide.place(x=170, y=300)
# Asigna un evento de clic
mensaje_olvide.bind("<Button-1>", recuperar_contraseña)  
# Bucle principal

root.mainloop()
