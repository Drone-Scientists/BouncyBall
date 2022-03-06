
# BouncyBall.py

# Head-Dev: December Redinger
# Drone Scientists Team: Alexis, Daniel, December, Everett, Levi, Tim

# Project Start: 1/23/2022
# Class: CS 320

# Feature: Ball will be pointed in a direction with a specific force and simulate the bounces.
# Feature: Ball will be able to change colors to suit the mood of the user.

from graphics import *
from math import *

# Maybe this problem can work in graphics. I'd have to figure out how to draw something and then re-draw it.
# First, let's get our window open.


class ballObject:

    def __init__(self):
        self.radius = 10
        self.velocity = 0
        self.acceleration = 0
        self.coordinatesx = 100
        self.coordinatesy = 100

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
    # coordinates is a Point data type
    def setCoordinates(self, coordinatesx, coordinatesy):
        self.coordinatesx = coordinatesx
        self.coordinatesy = coordinatesy

    # These functions get different values for the balls attributes

    def getRadius(self):
        return self.radius

    def getVelocity(self):
        return self.velocity

    def getAcceleration(self):
        return self.acceleration

    def getCoordinatesx(self):
        return self.coordinatesx

    def getCoordinatesy(self):
        return self.coordinatesy


class wallObject:

    def __init__(self):

        self.length = 50
        self.width = 10
        self.coordinatesx = 50
        self.coordinatesy = 50

    def setLength(self, length):
        self.length = length

    def setWidth(self, width):
        self.width = width

    def setCoordinates(self, coordinatesx, coordinatesy):
        self.coordinatesx = coordinatesx
        self.coordinatesy = coordinatesy

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getCoordinatesx(self):
        return self.coordinatesx

    def getCoordinatesy(self):
        return self.coordinatesy


# Defining velocity magnitude function

def vMagnitude(initialV, acceleration):

    # Velocity equals v0 plus acceleration
    velocity = initialV + acceleration
    return velocity


def directorAlgorithmX(direction, velMag):

    # The director algorithm X determines the X portion of the direction portion of the balls movement vector.
    # Negative values for X determine that the ball is moving left, positive values for X determine that the ball
    # is moving right.

    if direction == "left":

        xDirection = -velMag

    if direction == "right":

        xDirection = velMag

    # The return of this function is used for the X position delta.

    return xDirection


def directorAlgorithmY(direction, velMag):

    # The director algorithm Y determines the Y portion of the direction portion of the balls movment vector.
    # Negative values for Y determine that the ball is moving down, positive values for Y determine that the ball
    # is moving up.

    if direction == "down":

        yDirection = -velMag

    if direction == "up":

        yDirection = velMag

    return yDirection


def main():

    ball = ballObject()

    # Ball color is a variable that will be changeable later
    ballColor = "red"
    win = GraphWin("BouncyBall.py", 500, 500)
    dot = Circle(Point(ball.coordinatesx, ball.coordinatesy), ball.radius)
    dot.setFill(ballColor)
    dot.draw(win)
    win.getKey()


main()
