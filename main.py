import colorgram
import random
import turtle

# colors = colorgram.extract('hirst-color.jpg', 30)
#
# imported_colors = [
#     (color.rgb.r, color.rgb.g, color.rgb.b) for color in colors
# ]

color_list = [
    (132, 166, 205), (221, 148, 106), (32, 42, 61),
    (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71),
    (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49),
    (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188),
    (34, 151, 210), (65, 66, 56)
]


turtle.colormode(255)
screen = turtle.Screen()
screen.setup(width=700, height=700)
t = turtle.Turtle()
t.speed('fastest')
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)

# Draw the dots
dot_size = 20
dot_spacing = 50
for row in range(10):
    for column in range(10):
        t.dot(dot_size, random.choice(color_list))
        t.forward(dot_spacing)
    t.backward(dot_spacing * 10)
    t.left(90)
    t.forward(dot_spacing)
    t.right(90)

# Exit on click
screen.exitonclick()

