from turtle import *
import random

screen = Screen()
screen.setup(width=500,height=400)
is_game_on = False
user_bet = screen.textinput(title="guess a colour", prompt="bet a colour which will win on this turtle race? ")
color = ["red", "orange", "yellow", "blue", "purple", "green"]
y_position =[-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You've won! the Winner is {winner_color}")
            else:
                print(f"You've lost! the Winner is {winner_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
