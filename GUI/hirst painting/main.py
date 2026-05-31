# import colorgram
# color=colorgram.extract('fixed_image.jpg',15)
# print(color)
# rgb_colors=[]
# for colors in color:
#     r=colors.rgb.r
#     g=colors.rgb.g
#     b=colors.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import Turtle,Screen
import turtle as t
import random
turtle=Turtle()
screen=Screen()
t.colormode(255)
turtle.fillcolor('plum')
turtle.hideturtle()
turtle.speed('fastest')
turtle.setheading(220)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)
# turtle.setpos(-300, -200)
# screen.setup(width=800, height=600)
color_list=[(238, 238, 241), (240, 239, 238), (242, 117, 32), (241, 78, 93), (157, 113, 9), (240, 97, 29), (129, 215, 207), (212, 154, 163), (149, 186, 224), (85, 183, 4), (167, 45, 137), (51, 91, 87), (29, 36, 43), (133, 218, 221), (249, 208, 0)]
for _ in range (10):
    for _ in range(10):

        turtle.dot(20,(random.choice(color_list)))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.dot(20,(random.choice(color_list)))

    turtle.setheading(90)
    turtle.penup()
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.rt(-180)
# for _ in range (10):
#     turtle.setheading(180)
#     turtle.dot(20,(random.choice(color_list)))
#     turtle.penup()
#     turtle.forward(50)
#     turtle.pendown()
# turtle.dot(20,(random.choice(color_list)))
# turtle.setheading(90)
# turtle.penup()
# turtle.forward(50)
# turtle.dot(20, (random.choice(color_list)))
# turtle.setheading(180)


screen.exitonclick()
