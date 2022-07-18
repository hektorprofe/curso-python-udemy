import sqlite3
from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Bar Don Costa - Menú")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="   Bar Don Costa   ", fg="darkgreen", font=("Times New Roman",28,"bold italic")).pack()
Label(root, text="Menú del día", fg="green", font=("Times New Roman",24,"bold italic")).pack()

# Separación de títulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante_final.db")
cursor = conexion.cursor()

# Buscar las categorías y platos de la bd
categorias = cursor.execute("SELECT * FROM categoria").fetchall()	
for categoria in categorias:
	Label(root, text=categoria[1], fg="black", font=("Times New Roman",20,"bold italic")).pack()

	platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
	for plato in platos:
		Label(root, text=plato[1], fg="gray", font=("Verdana",15,"italic")).pack()

	# Separación entre categorias
	Label(root, text="").pack()	

conexion.close()

# Precio del menú
Label(root, text="12€ (IVA incl.)", fg="darkgreen", font=("Times New Roman",20,"bold italic")).pack(side="right")

# Finalmente ejecutamos el bucle
root.mainloop()