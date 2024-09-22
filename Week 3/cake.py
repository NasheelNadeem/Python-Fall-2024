import turtle

def location(x,y):
    turtle.penup
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    


def draw_table(width,height):
    turtle.penup
    location()
    turtle.pendown
    turtle.goto(width, height)

def main():
    x=int(input("x loacation?"))
    y=int(input("y loacation?"))
    location(x,y)
    width=int(input("x width?"))
    height=int(input("y height?"))
    draw_table(width,height)

main()