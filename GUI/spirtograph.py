from turtle import Turtle,Screen
import random
turtle=Turtle()
turtle.speed(0)
turtle.hideturtle()
for i in range (0,250):
    color = random.choice(['red', 'blue', 'green', 'yellow', 'orange', 'plum', 'black', 'violet',])
    turtle.pencolor(color)
    turtle.rt(i)
    turtle.circle(100)
screen=Screen()
screen.exitonclick()