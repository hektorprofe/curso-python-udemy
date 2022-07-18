# www.tutorialspoint.com/python/python_gui_programming.htm


"""from tkinter import *

def selec():

    cadena = ""
    if (leche.get()): cadena += "Con leche"
    else: cadena += "Sin leche"

    if (azucar.get()): cadena += " y con azúcar"
    else: cadena += " y sin azúcar"

    monitor.config(text=cadena)

root = Tk()
root.config(bd=10)

leche = IntVar()    # 1 si, 0 no
azucar = IntVar()   # 1 si, 0 no

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side=LEFT)

frame = Frame(root).pack(side=RIGHT)
Label(frame, text="¿Cómo quieres el café?\n").pack(anchor=W)
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=selec).pack(anchor=W)
Checkbutton(frame, text="Con azúcar", variable=azucar, onvalue=1, offvalue=0, command=selec).pack(anchor=W)

monitor = Label(frame)
monitor.pack()

root.mainloop()




root = Tk()

imagen = PhotoImage(file="imagen.gif")
label = Label(root, image=imagen, bd=0).pack()

root.mainloop()


from tkinter import *
def selec():
    monitor.config(text = "Opción {}".format(opcion.get() ) )

def reset():
    opcion.set(None)
    monitor.config(text='')

root = Tk()
root.config(bd=15)

opcion = IntVar() # Como StrinVar pero en entero

Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=selec).pack()
Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=selec).pack()
Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=selec).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()


from tkinter import *

# Funciones backend
def borrar():
    n1.set('')
    n2.set('')

def sumar():
    r.set( float( n1.get() ) + float(n2.get() ) )
    borrar()

def restar():
    r.set( float( n1.get() ) - float(n2.get() ) )
    borrar()

def multiplicar():
    r.set( float( n1.get() ) * float(n2.get() ) )
    borrar()

# Estructura del formulario
root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Numero 1").pack()
Entry(root, justify=CENTER, textvariable=n1).pack()

Label(root, text="\nNumero 2").pack()
Entry(root, justify=CENTER, textvariable=n2).pack()

Label(root, text="\nResultado").pack()
Entry(root, justify=CENTER, state=DISABLED, textvariable=r).pack()

Label(root).pack() # Separador
button = Button(root, text="Sumar", command=sumar).pack(side=LEFT)
button = Button(root, text="Restar", command=restar).pack(side=LEFT)
button = Button(root, text="Multiplicar", command=multiplicar).pack(side=LEFT)

root.mainloop()


from tkinter import *

root = Tk()

label = Label(root, text="Nombre")
label.grid(row=0,column=0, sticky=W, padx=5, pady=5)

entry = Entry(root, justify=RIGHT, state=DISABLED)
entry.grid(row=0,column=1, padx=5, pady=5)

label2 = Label(root, text="Apellidos")
label2.grid(row=1,column=0, sticky=W, padx=5, pady=5)

entry2 = Entry(root, justify=CENTER, show="?")
entry2.grid(row=1,column=1, padx=5, pady=5)

root.mainloop()


# www.tutorialspoint.com/python/python_gui_programming.htm
from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

label = Label(root, text="¡Hola Mundo!")
label.pack(anchor=NW)

label2 = Label(root, text="¡Otra etiqueta!")
label2.pack(anchor=CENTER)
label2.config(fg="blue", bg="green", font=("Verdana",24))


label3 = Label(root, text="¡Última etiqueta!")
label3.pack(anchor=SE)

texto2 = StringVar()
label2.config(textvariable=texto2)
texto2.set("Un nuevo texto")

root.mainloop()


from tkinter import *
root = Tk()
root.title("Hola mundo")  # Título de la ventana
root.iconbitmap('hola.ico') # Icono de la ventana, abajo no intérprete -> compilada

frame = Frame(root)  # Hijo de root, no ocurre nada
frame.pack()      # Empaqueta el frame en la raíz. Como no tenemos
        # ningún elemento dentro del frame, éste no tiene
        # tamaño y aparece ocupando lo mínimo posible, 0*0 pixels
frame.config(width=480,height=320) # Podemos establecer un tamaño
                         # La raíz se adapta al frame que contiene
# También podemos añadir la configuración al crear el frame
Frame(root, width=480,height=320) 

frame.config(bg="lightblue")     # color de fondo, background
frame.config(cursor="arrow")   # tipo de cursor
frame.config(relief="ridge")      # relieve del frame
frame.config(bd=25)             # tamaño del borde en píxeles

frame.pack(side=RIGHT) # a la derecha al medio
frame.pack(anchor=SE)  # sudeste, abajo a la derecha

root.config(bg="blue")          # color de fondo, background
root.config(cursor="pirate")    # tipo de cursor (arrow defecto)
root.config(relief="sunken")    # relieve del frame
root.config(bd=25)      # tamaño del borde en píxeles

root.mainloop()

from tkinter import *
root = Tk()
Label(root, text="¡Hola Mundo!").pack(anchor=NW)
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor=CENTER)
Label(root, text="¡Última etiqueta!").pack(anchor=SE)

label.pack(anchor=CENTER)
label.config(fg="blue", bg="green", font=("Verdana",24)) # foreground, background

root.mainloop()


from tkinter import *
def algo():
   pass
root = Tk()
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar", command=algo)
editmenu.add_command(label="Copiar", command=algo)
editmenu.add_command(label="Pegar", command=algo)
menubar.add_cascade(label="Editar", menu=editmenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda", command=algo)
helpmenu.add_command(label="Acerca de...", command=algo)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()

from tkinter import *
root = Tk()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()



from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

def test():
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero",mode='w', defaultextension=".txt")
    fichero.write("Hola!")
    fichero.close()

root = Tk()

Button(root, text="Clícame", command=test).pack()

root.mainloop()"""

from tkinter import *
from tkinter import filedialog as FileDialog

ruta = ''

def nuevo():
    mensaje.set('Nuevo fichero.')
    texto.delete(1.0, END)  # En flotante, el primer caracter es un salto
    root.title("Mi editor")  # Reiniciamos el título por si lo hemos cambiado
    ruta = ""  # Reiniciamos la ruta por si hemos abierto un fichero


def abrir():
    global ruta
    ruta = FileDialog.askopenfilename(
        filetypes=(("Ficheros de texto", "*.txt"),), title="Abrir un fichero.")

    if ruta != "":  # Si la ruta es válida abrimos el contenido en modo lectura
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')  # Nos aseguramos de que esté vacío
        texto.insert('insert', contenido)  # Le insertamos el texto del fichero
        fichero.close()
        mensaje.set('Abrir fichero.')
        root.title(ruta + " - Mi editor")
    else:
        mensaje.set('Abrir fichero cancelado.')


def guardar():
    global ruta
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')  # recuperamos el texto
        fichero = open(ruta, 'w+') # creamos el fichero o abrimos
        fichero.write(contenido)  # escribimos el texto
        fichero.close()
        mensaje.set('Fichero guardado correctamente.')
        root.title(ruta + " - Mi editor")
    else:
        guardar_como()


def guardar_como():
    global ruta
    fichero = FileDialog.asksaveasfile(title="Guardar fichero como", mode='w+', filetypes=(("Ficheros de texto", "*.txt"),), defaultextension=".txt")
    ruta = fichero.name  # El atributo name es la ruta
    if fichero is not None:
        contenido = texto.get(1.0, 'end-1c')  # recuperamos el texto
        fichero.write(contenido)  # escribimos el texto
        fichero.close()
        mensaje.set('Fichero guardado correctamente.')
        root.title(ruta + " - Mi editor")
    else:
        mensaje.set('Guardado cancelado.')



# La ventana no se podrá redimensionar
root = Tk()
root.title("Mi editor")

# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

# Caja de texto central
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(padx=6, pady=4, bd=0, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(root, textvar=mensaje, justify='right')
monitor.pack(side='left')

# Menú y bucle de la aplicación
root.config(menu=menubar)
root.mainloop()
