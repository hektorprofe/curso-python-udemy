import turtle
import sys

window = turtle.Screen()
window.title("Aproximación a los videojuegos")
window.bgcolor("#68a0ed")
window.setup(500, 500)


class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")
        self.color("darkgreen")

    def adelante(self):
        self.forward(10)

    def atras(self):
        self.backward(10)

    def izquierda(self):
        self.left(15)

    def derecha(self):
        self.right(15)


# Creamos la tortuga e iniciamos el bucle
kame = Tortuga()

# Mapeamos los métodos en eventos de teclado
window.onkey(kame.izquierda, "a")
window.onkey(kame.adelante, "w")
window.onkey(kame.derecha, "d")
window.onkey(kame.atras, "s")
window.onkey(sys.exit, "e")

# Ponemos la ventana a esuchar eventos
window.listen()

# Iniciamos el bucle
turtle.mainloop()
