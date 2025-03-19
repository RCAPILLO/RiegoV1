from tkinter import Tk
from .Inicio import VentanaInicio

from Clases.Riego import Riego  # Ahora debería funcionar correctamente

# Configuración de la ventana principal
def main():
    root = Tk()
    app = VentanaInicio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
