import turtle
import sys

window = turtle.Screen()
window.title("Aproximación a los videojuegos")
window.bgcolor("#68a0ed")
window.setup(500, 500)
window.setworldcoordinates(0, 500, 500, 0)


class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")
        self.color("darkgreen")
        self.velocidad = 0
        self.velocidad_maxima = 20

    def mover(self):

        orden = turtle.textinput(
            "Orden requerida",
            "Movimientos: A W S D")

        if orden:
            if orden.lower() == "d":
                self.setheading(0)
            elif orden.lower() == "w":
                self.setheading(270)
            elif orden.lower() == "a":
                self.setheading(180)
            elif orden.lower() == "s":
                self.setheading(90)
            else:
                return
        else:
            sys.exit()

        # Movemos la tortuga
        self.forward(100)


kame = Tortuga()
while 1:
    kame.mover()
