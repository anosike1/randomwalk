# import turtle
from turtle import *
from random import *

# create an object called t based on the Turtle class
t=Turtle()
# create it the shape of a turtle 
t.shape("turtle")
# create a colormode of 255. This will be used in the creation of colors eventually
colormode (255)

# create a fucntion which creates an RGB color combination by
def x():
    #...assigning random values to R, G, and B
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    #...and then creating a tuple made up of the combination
    col = (r, g, b)
    # this tuple will be returned
    return col

# create a list of directions that will be moved (0,90,180, and 270 degrees)
direction = [0,90,180,270]
# increase the pensize to 5
t.pensize(5)
# and increase the speed to fastest
t.speed ("fastest")

# create a for loop that runs 200 times
# each time, it moves forward 30 paces, in a random direction selected from the list
for _ in range (200):
    t.forward (30)
    t.setheading(choice(direction))
# at each run, the color changes based on the created color
    t.color(x())

# create a screen object and 
# activate exit on click - so that the screen exits when clicked
screen=Screen()
screen.exitonclick()