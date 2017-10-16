# def suma(num1, num2):
#     return num1 + num2
#
# res = suma(2,3)
# print(res)


import turtle

def main():
    window = turtle.Screen()
    rafa = turtle.Turtle()
    make_square(rafa)

def make_square(rafa):
    length = int(input('Tamaño del cuadrado: '))
    for i in range(4):
        make_line_and_turn(rafa, length)
    turtle.mainloop()

def make_line_and_turn(rafa, length):
    rafa.forward(length)
    rafa.left(90)

if __name__ == '__main__':
    main()
