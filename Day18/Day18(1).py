# from turtle import Turtle, Screen
# tt_turtle_obj = Turtle()
#
# tt_turtle_obj.shape("turtle")
# tt_turtle_obj.color("green")
#
# for _ in range(15):
#     tt_turtle_obj.forward(10)
#     tt_turtle_obj.penup()#allows to move forward without drawing
#     tt_turtle_obj.forward(10)
#     tt_turtle_obj.pendown()#allows to draw
#
# screen = Screen()
# screen.exitonclick()


# import random
# import turtle as t
# timmy = t.Turtle()
# colors = ["cyan","medium spring green","green yellow","misty rose","medium purple","lavender","light salmon","sandy brown"]
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         timmy.forward(100)
#         timmy.right(angle)
# for shape_side_n in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

# import random
# import turtle as t
# timmy = t.Turtle()
# colors = ["cyan","medium spring green","green yellow","misty rose","medium purple","lavender","light salmon","sandy brown"]
# timmy.pensize(10)
# timmy.speed("fastest")
# directions = [0,90,180,270]
#
# for _ in range(200):
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#
# import random
# import turtle as t
# timmy = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
# timmy.pensize(10)
# timmy.speed("fastest")
# directions = [0,90,180,270]
#
# for _ in range(200):
#     random_color()
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

import random
import turtle as t
timmy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



timmy.speed("fastest")

def draw_spirograph(size_of_the_gap):
    for _ in range(int(360 / size_of_the_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_the_gap)
draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()