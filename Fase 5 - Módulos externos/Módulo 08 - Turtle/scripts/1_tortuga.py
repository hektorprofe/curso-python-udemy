import turtle

window = turtle.Screen()
window.title("Pruebas con turtle")
window.bgcolor("#68a0ed")
window.setup(500, 500)

kame = turtle.Turtle()
kame.shape("turtle")
kame.color("darkgreen")
kame.pensize(2)
kame.speed(10)

for i in range(0, 6):
    kame.penup()
    kame.goto(i, -i*25)
    kame.pendown()
    kame.circle(i*25)

turtle.mainloop()
