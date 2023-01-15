
import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    
    make_square(dave)

    turtle.mainloop()

def make_square(dave):
    length = int(raw_input("tamaño del la ventana:"))
    make_line_turn(dave, length)

def make_line_turn(dave, length):

    dave.forward(length)
    dave.left(90)

    for i in range(4):
        make_line_turn(dave, length)

    
if __name__ == '__main__':
    main()
