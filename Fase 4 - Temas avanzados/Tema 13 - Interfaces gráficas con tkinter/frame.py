from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('hola.ico')


frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")


root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")


# Finalmente bucle de la apliación
root.mainloop()