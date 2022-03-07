
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


def directorAlgorithmX(angle, velMag):

    # The director algorithm X takes in an angle and a velocity to figure out the X vector component.

    xComponent = cos(angle) * velMag

    return xComponent


def directorAlgorithmY(angle, velMag):

    # The director algorithm Y takes in an angle and a velocity to figure out the Y vector component.

    yComponent = sin(angle) * velMag

    return yComponent


def directorAlgorithmV(xComponent, yComponent):

    # This function takes the xComponent vector and the yComponent vector and returns a combined velocity!

    newVector = sqrt((xComponent * xComponent) + (yComponent * yComponent))

    return newVector

# We need a function that provides an angle, otherwise the director algorithms do not work.


def velocityDelta(initialV, initialAngle, acceleration):

    # This function calculates a new velocity. The change in Y component is important here.

    x = directorAlgorithmX(initialAngle, initialV)
    newY = directorAlgorithmY(initialAngle, initialV) - acceleration

    # With x and newY , we can create the new velocity magnitude

    newV = directorAlgorithmV(x, newY)

    return newV


def main():

    ball = ballObject()
    wall1 = wallObject()
    wall2 = wallObject()
    wall3 = wallObject()
    wall4 = wallObject()

    wall3.setLength(10)
    wall3.setWidth(50)
    wall4.setLength(10)
    wall4.setWidth(50)

    # Ball color is a variable that will be changeable later
    ballColor = "red"
    win = GraphWin("BouncyBall.py", 500, 500)
    wallA = Rectangle(Point(0, 0), Point(500, 10))
    wallB = Rectangle(Point(0, 0), Point(10, 500))
    wallC = Rectangle(Point(490, 0), Point(500, 500))
    wallD = Rectangle(Point(0, 490), Point(500, 500))
    dot = Circle(Point(ball.coordinatesx, ball.coordinatesy), ball.radius)
    wallA.setFill("blue")
    wallB.setFill("blue")
    wallC.setFill("blue")
    wallD.setFill("blue")
    dot.setFill(ballColor)

    dot.draw(win)
    wallA.draw(win)
    wallB.draw(win)
    wallC.draw(win)
    wallD.draw(win)

    win.getKey()


main()
