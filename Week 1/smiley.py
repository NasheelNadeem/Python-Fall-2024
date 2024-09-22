import turtle
turtle.speed(10)
def draw_circle(x,y,radius,fill_color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.setheading(0)


def draw_centered_circle(x,y,radius,fill_color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.setheading(0)
    



def draw_eye(x,y,radius,fill_color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.setheading(0)

def draw_mouth(x,y,radius,fill_color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.left(90)
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(radius,180)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)


def main():
    draw_circle(0,0,200,"yellow")
    draw_centered_circle(0,0,50,"pink")
    draw_eye(80,80,30,"white")
    draw_eye(-80,80,30,"white")
    draw_eye(80,80,20,"blue")
    draw_eye(-80,80,20,"blue")
    draw_eye(80,80,10,"black")
    draw_eye(-80,80,10,"black")
    draw_mouth(90,-150,100,"black")
    input("press")
turtle.tracer(False)
main()