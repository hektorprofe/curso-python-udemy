from tkinter import *

# Configuración de la raíz
root = Tk()


texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas",12), padx=15, pady=15, selectbackground="red")


# Finalmente bucle de la apliación
root.mainloop()