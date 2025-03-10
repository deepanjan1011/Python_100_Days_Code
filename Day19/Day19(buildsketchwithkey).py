from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():#this is a move function with no args
    timmy.forward(10)
def move_backward():
    timmy.backward(10)
def move_counter_clock():
    timmy.left(10)
def move_clock_wise():
    timmy.right(10)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()

screen.listen()
screen.onkey( key="w",fun=move_forward)
screen.onkey( key="s",fun=move_backward)
screen.onkey( key="a",fun=move_counter_clock)
screen.onkey( key="d",fun=move_clock_wise)
screen.onkey( key="c",fun=clear)

screen.exitonclick()
