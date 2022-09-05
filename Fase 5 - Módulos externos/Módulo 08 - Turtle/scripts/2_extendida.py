import turtle
import math

window = turtle.Screen()
window.title("Extendiendo una tortuga")
window.bgcolor("#68a0ed")
window.setup(500, 500)
window.setworldcoordinates(0, 500, 500, 0)


class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")

    def rectangulo(self, x, y, ancho, alto, color="black"):
        self.color(color)
        self.penup()
        self.goto(x+ancho/2, y+alto/2)
        self.pendown()
        self.goto(x-ancho/2, y+alto/2)
        self.goto(x-ancho/2, y-alto/2)
        self.goto(x+ancho/2, y-alto/2)
        self.goto(x+ancho/2, y+alto/2)

    def poligono(self, lados, radio, color="black"):
        self.color(color)
        # Calculamos el ángulo de cada porción
        angulo = 2 * math.pi / lados
        # Calculamos la posición del primer vértice
        # x = radio por seno del ángulo
        # y = radio por coseno del ángulo
        # Le sumamos el offset del centro del lienzo
        ancho_ventana = turtle.screensize()[0]/2
        alto_ventana = turtle.screensize()[1]/2
        x = ancho_ventana + radio * math.sin(angulo)
        y = alto_ventana + radio * math.cos(angulo)
        # Posicionamos la tortuga sin dejar rastro y bajamos la pluma
        self.penup()
        self.goto(x, y)
        self.pendown()
        # Calculamos la posición de los siguientes vértices trazando las líneas
        for i in range(lados+1):
            x = ancho_ventana + radio * math.sin(i * angulo)
            y = alto_ventana + radio * math.cos(i * angulo)
            self.goto(x, y)


kame = Tortuga()
kame.speed(11)  # Velocidad maxima
for n in range(3, 25):
    kame.poligono(n, n*10)

turtle.mainloop()
