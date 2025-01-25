from tkinter import Tk
from Inicio import VentanaInicio


# Configuración de la ventana principal
def main():
    root = Tk()
    app = VentanaInicio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
