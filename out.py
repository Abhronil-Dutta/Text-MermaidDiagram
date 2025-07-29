import random
import time
import turtle
turtle.tracer(1, 0) # Make the turtle draw faster.

# Set up the constants:
NUM_SEGMENTS = 8
SIZE = 300
WAIT_TIME = 1000

def main():
    # Set up the window:
    turtle.setworldcoordinates(-SIZE / 2 - 50, -200, SIZE / 2 + 50, 250)
    turtle.hideturtle()

    # Draw the background:
    turtle.penup()
    turtle.pensize(2)
    turtle.pencolor('white')
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(SIZE + 100)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(SIZE + 100)
    turtle.end_fill()

    # Draw the clock hands:
    for i in range(NUM_SEGMENTS):
        turtle.penup()
        turtle.home()
        turtle.right(i * (360 / NUM_SEGMENTS))
        turtle.pendown()
        turtle.forward(SIZE / 2)
        time.sleep(WAIT_TIME / 1000)

    turtle.done()