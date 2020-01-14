# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)

    turtle.mainloop()

def make_square(dave):
    for i in range(4):
        make_line_and_turn(dave, 100)

def make_line_and_turn(dave, lenght):
    dave.forward(lenght)
    dave.left(90)

if __name__ == '__main__':
    main()