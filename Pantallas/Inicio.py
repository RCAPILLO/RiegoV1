from tkinter import *
import mysql.connector
from Principal import mostrar_pantalla_principal
from tkinter import messagebox

class VentanaInicio:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de riego V.1")
        self.master.geometry("500x500")
        self.master.iconbitmap("Imagenes/LogoRiegoV1.ico")
        self.master.resizable(0, 0)

        # Configuración del marco
        self.miframe = Frame(self.master, width=500, height=400)
        self.miframe.pack()

        # Etiquetas de título 
        Label(self.miframe, text="Sistema de Riego", font=("Comic Sans MS", 24), justify="center").place(x=120, y=20)
        # Línea horizontal decorativa
        Frame(self.miframe, bg="black", height=2, width=460).place(x=20, y=80)
        # Etiquetas de casillas para iniciar sesion
        Label(self.miframe, text="Usuario", font=("Comic Sans MS", 16)).place(x=20, y=120)
        Label(self.miframe, text="Password", font=("Comic Sans MS", 16)).place(x=20, y=180)

        # Campos de entrada
        self.usuario = Entry(self.miframe, font=("Arial", 14))
        self.usuario.place(x=140, y=120, width=200)
        self.pasword = Entry(self.miframe, font=("Arial", 14), show="*")
        self.pasword.place(x=140, y=180, width=200)

        # Mensaje de error inicializado como un Label vacío
        self.mensaje_error = Label(self.miframe, text="", font=("Arial", 12), fg="red")
        self.mensaje_error.place(x=140, y=220)  # Posiciona el mensaje de error en la pantalla

        # Botón de inicio
        iniciar = Button(self.miframe, text="Iniciar Sesión",width=12,height=1, font=("Arial", 14), bg="lightblue", command=self.validar_usuario, cursor="hand2")
        iniciar.place(x=180, y=250)

        # Mensaje "Olvidé mi contraseña" (con evento de clic)
        mensaje_olvide = Label(self.miframe, text="Olvidé mi contraseña", font=("Arial", 12), fg="blue", cursor="hand2")
        mensaje_olvide.place(x=170, y=300)
        # Asigna un evento de clic
        mensaje_olvide.bind("<Button-1>", self.recuperar_contraseña)

        # Botón de Cancelar
        cancelar = Button(self.miframe, text="Cancelar", width=12, height=1, font=("Arial", 14), bg="lightblue", command=self.cancelar, cursor="hand2")
        cancelar.place(x=180, y=350)

    # Conexión a la base de datos MySQL
    def conectar_bd(self):
        return mysql.connector.connect(
            host="localhost",       # Servidor local
            user="root",            # Usuario de MySQL 
            password="",            # Contraseña de MySQL 
            database="riego"        # Nombre de la base de datos
        )

    # Función para validar usuario y contraseña desde la base de datos
    def validar_usuario(self):
        usuario_input = self.usuario.get()
        pasword_input = self.pasword.get()

        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()

            # Consulta para verificar usuario y contraseña
            cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND password = %s", 
                           (usuario_input, pasword_input))
            resultado = cursor.fetchone()
            conn.close()

            if resultado:
                # Si las credenciales son correctas, abrir nueva ventana
                messagebox.showinfo("Inicio de Sesión", "Bienvenido al sistema de riego v1")
                self.master.destroy()  # Cerrar la ventana actual
                mostrar_pantalla_principal()  # Llamar a la pantalla principal
            else:
                self.mensaje_error["text"] = "Usuario o contraseña incorrectos"
        except mysql.connector.Error as err:
            self.mensaje_error["text"] = f"Error de conexión: {err}"

    # Función para manejar el evento de "Olvidé mi contraseña"
    def recuperar_contraseña(self, event):
        # Mostrar un mensaje en consola por ahora (puedes agregar más lógica aquí)
        print("Redirigir a la página de recuperación de contraseña")

    def cancelar(self):
        self.master.destroy()  # Cierra la ventana actual