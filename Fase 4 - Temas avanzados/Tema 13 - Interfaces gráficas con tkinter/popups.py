from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

# Configuración de la raíz
root = Tk()


def test():
	# MessageBox.showinfo("Hola!","Hola mundo")
	# MessageBox.showwarning("Alerta","Sección sólo para administradores.")
	# MessageBox.showerror("Error!","Ha ocurrido un error inesperado.")
	# resultado = MessageBox.askquestion("Salir","¿Está seguro que desea salir sin guardar?")
	# if resultado == "yes":  # "no"
	#	root.destroy()
	# resultado = MessageBox.askokcancel("Salir","¿Sobreescribir el fichero actual?")
	# resultado = MessageBox.askyesno("Salir","¿Está seguro que desea salir sin guardar?")
	#if resultado:
	#	root.destroy()
	#resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
	#if resultado:
	#	root.destroy()
	#color = ColorChooser.askcolor(title="Elige un color")
	#print(color)
	#ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", 
	#	filetypes=(("Fichero de texto","*.txt"),
	#		("Fichero de texto avanzado","*.txt2"),
	#		("Todos los ficheros","*.*")) )
	#print(ruta)
			# equivale a open('ruta','w')
	fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt") 
	if fichero is not None:
		fichero.write("Hola voy a escribir otra cosa!")
		fichero.close()


Button(root, text="Clícame", command=test).pack()


# Finalmente bucle de la apliación
root.mainloop()