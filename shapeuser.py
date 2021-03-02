from turtle import *

tim = Turtle()


screen = Screen()


def move_forward():
    tim.forward(50)


def move_back():
    tim.bk(50)


def right():
    newheading = tim.heading() - 10
    tim.setheading(newheading)


def left():
    newheading = tim.heading() + 10
    tim.setheading(newheading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()