
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


class ballObject:

    def __init__(self):
        self.radius = 10
        self.velocity = 0
        self.acceleration = 0
        self.coordinates = Point(100, 100)

    # These functions set different variables for the ball

    # Radius function determines how large the ball is.
    def setRadius(self, radius):
        self.radius = radius

    # Velocity function determines how fast the ball is moving.
    def setVelocity(self, velocity):
        self.velocity = velocity

    # Acceleration function determines how fast the velocity of the ball is changing.
    def setAcceleration(self, acceleration):
        self.acceleration = acceleration

    # Coordinates function determines where the ball is on the coordinates
    def setCoordinates(self, coordinates):  # coordinates is a Point data type
        self.coordinates = coordinates

    # These functions get different values for the balls attributes

    def getRadius(self):
        return self.radius

    def getVelocity(self):
        return self.velocity

    def getAcceleration(self):
        return self.acceleration

    def getCoordinates(self):
        return self.coordinates


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
