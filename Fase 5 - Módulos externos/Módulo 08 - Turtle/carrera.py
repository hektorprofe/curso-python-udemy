import turtle
import random
import tkinter

screen = turtle.Screen()
screen.title("Carrera de tortugas")
screen.setup(600, 400)
screen.bgcolor("#68a0ed")
screen.setworldcoordinates(0, 400, 600, 0)

# Creamos una lista para las tortugas
tortugas = []
# Creamos una lista con los colores
colores = ["yellow", "orange", "red", "brown", "purple",
           "blue", "cyan", "green", "black", "white"]

# Para cada color creamos una tortuga
for index, color in enumerate(colores):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(color)
    tortuga.speed(4)
    tortuga.penup()
    tortuga.goto(10, index*40+15)
    tortuga.pendown()
    # La añadimos a la lista
    tortugas.append(tortuga)

# Generamos un bucle infinito para mover las tortugas aleatoriamente
run = True
while run:
    # Para cada tortuga
    for tortuga in tortugas:
        # Generamos una distancia aleatoria
        distancia = random.randint(0, 25)
        # La movemos esa distancia
        tortuga.forward(distancia)
        # Si alguna llega al margen derecho
        if tortuga.position()[0] >= 560:
            # Mostramos un mensaje en un cuadro de diálogo
            tkinter.messagebox.showinfo(
                title="Fin de la carrera",
                message=f"Ha ganado la tortuga {tortuga.color()[0].capitalize()}")
            # Finalizamos el bucle infinito
            run = False
            break

turtle.mainloop()
