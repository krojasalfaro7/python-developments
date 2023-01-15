# File name: turtle_test.py
# Author: Kevin Rojas
# email: krojas.alfaro7@gmail.com
# Python Version: 3.8
# Practica del modulo turtle
from builtins import print
try:
    import turtle
    print("Works OK")
except:
    print("An error has occurred")


def turtle_do_draw(turtle_name, window, movimientos, distancia=100):
    for _ in range(movimientos):
        turtle_name.forward(distancia)
        turtle_name.left(360/movimientos)
    window.exitonclick()

def turtle_do_shape(turtle_name, window, movimientos, angulo, distancia=200, **argv):
    if 'speed' in argv:
        print(argv['speed'])
        turtle_name.speed(argv['speed'])
    for _ in range(movimientos):
        turtle_name.forward(distancia)
        turtle_name.left(angulo)

    turtle_name.left(180)
    turtle_name.forward(400)
    turtle_name.left(180)
    for _ in range(movimientos):
        turtle_name.forward(distancia)
        turtle_name.left(angulo)


    turtle_name.left(180)
    turtle_name.forward(400)
    turtle_name.left(180)
    for _ in range(movimientos):
        turtle_name.forward(distancia)
        turtle_name.left(angulo)
    window.exitonclick()

if __name__ == '__main__':
    #Defining the objects
    wn = turtle.Screen()
    kevin = turtle.Turtle()

    #Draw a square
    #turtle_do_draw(turtle_name=kevin, window=wn, movimientos=4)

    # Draw an equilateral triangle
    #turtle_do_draw(turtle_name=kevin, window=wn, movimientos=3)

    # Draw a hexangon
    #turtle_do_draw(turtle_name=kevin, window=wn, movimientos=6)

    # Draw a octogon
    #turtle_do_draw(turtle_name=kevin, window=wn, movimientos=8)

    # Draw a shape
    #turtle_do_shape(turtle_name=kevin, window=wn, angulo=216, movimientos=8, distancia=400)

    # Draw a shape
    turtle_do_shape(turtle_name=kevin, window=wn, angulo=225, movimientos=8, distancia=400, speed=10)