
# BouncyBall.py

# Head-Dev: December Redinger
# Drone Scientists Team: Alexis, Daniel, December, Everett, Levi, Tim

# Project Start: 1/23/2022
# Class: CS 320

# Feature: Ball will be pointed in a direction with a specific force and simulate the bounces.
# Feature: Ball will be able to change colors to suit the mood of the user.

from graphics import *


# Maybe this problem can work in graphics. I'd have to figure out how to draw something and then re-draw it.
# First, let's get our window open.

def main():

    # pt is a placeholder point that will be replaced with a mousehandler
    pt = Point(100, 100)

    # Ball color is a variable that will be changeable later
    ballColor = "red"
    win = GraphWin("BouncyBall.py", 500, 500)
    ball = Circle(pt, 10)
    ball.setFill(ballColor)
    ball.draw(win)
    win.getKey()


main()
