import turtle as t
from turtle import Turtle, Screen
import random
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

t.colormode(255)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (12, 70, 64), (168, 99, 102),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (107, 127, 153), (176, 192, 208)]
puck = Turtle()


def horizontal_dots(dots_num):
    for _ in range(dots_num):
        dot_color = random.choice(color_list)
        puck.dot(20, dot_color)
        puck.forward(50)


puck.penup()
puck.setposition((-225, -225))
puck_y = -225
for _ in range(10):
    horizontal_dots(10)
    puck_y += 50
    puck.setx(-225)
    puck.sety(puck_y)

puck.hideturtle()

screen = Screen()
screen.exitonclick()
