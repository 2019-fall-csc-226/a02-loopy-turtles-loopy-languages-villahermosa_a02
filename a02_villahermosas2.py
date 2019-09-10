######################################################################
# Author: Shawn Villahermosa
# Username: villahermosas
#
# Assignment: A02: Loopy Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes
######################################################################
# Acknowledgements:
#
# originally created by Shawn Villahermosa
#
# took some inspirations on a02_think_cs.py, a02_triple_turtles.py, and a02_turtle_house.py
#
# copied a little bit of code on writing the text "Smile!!!" on a02_think_cs.py
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle

# Initializes the screen
wn = turtle.Screen()
wn.title("This Makes Me Happy")
wn.screensize(100)
wn.bgcolor("black")

# Makes the turtles
eyes = turtle.Turtle()         # The eye turtle
eyes.hideturtle()

hat = turtle.Turtle()          # The hat turtle
hat.hideturtle()

smile = turtle.Turtle()        # The smile turtle
smile.hideturtle()

text = turtle.Turtle()         # The text turtle
text.color("dark blue")
text.pensize(5)
text.speed(5)
text.hideturtle()
text.penup()

# Setting the hat
hat.penup()
hat.left(90)
hat.forward(65)
hat.right(90)
hat.forward(55)
hat.pendown()

# Making the hat
hat.color("purple")
hat.begin_fill()
for sides in range(3):
    hat.left(120)
    hat.forward(133)
hat.end_fill()

# Setting the eyes
eyes.penup()
eyes.backward(75)
eyes.pendown()

# Make the eyes
eyes.color("red1")
eyes.begin_fill()
for edges in range(4):
    eyes.forward(50)
    eyes.left(90)
eyes.end_fill()

eyes.penup()
eyes.forward(75)
eyes.pendown()

eyes.begin_fill()
for edges in range(4):
    eyes.forward(50)
    eyes.left(90)
eyes.end_fill()

# Setting the smile
smile.penup()
smile.forward(50)
smile.right(90)
smile.forward(10)
smile.right(90)
smile.forward(-20)
smile.left(90)
smile.pendown()

# Making the smile
smile.pensize(5)
smile.color("yellow")
smile.forward(65)
smile.right(90)
smile.forward(165)
smile.right(90)
smile.forward(65)

# Writing the word "Smile!!!"
tList = [text]
texts = tList[0]

texts.setpos(0, -180)
texts.write("Smile!!! ", move=False, align='center', font=("TimesNewRoman", 50, ("bold", "normal")))

wn.exitonclick()
