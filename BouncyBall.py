
# BouncyBall.py

# Head-Dev: December Redinger
# Drone Scientists Team: Alexis, Daniel, December, Everett, Levi, Tim

# Project Start: 1/23/2022
# Class: CS 320

# Feature: Ball will be pointed in a direction with a specific force and simulate the bounces.
# Feature: Ball will be able to change colors to suit the mood of the user.

from graphics import *
from math import *
import unittest
import turtle
import time

# Maybe this problem can work in graphics. I'd have to figure out how to draw something and then re-draw it.
# First, let's get our window open.

# This is the test class for the bouncyball simulation.


class TestBB(unittest.TestCase):

    def test_directorXFlatAngle(self):
        result = cos(0) * 15
        self.assertEqual(result, 15)

    def test_directorXFortyFiveAngle(self):
        result = cos(45) * 15
        result = round(result)
        self.assertEqual(result, 8)


class ballObject:

    def __init__(self):
        self.radius = 10
        self.velocity = 0
        self.acceleration = 0
        self.coordinatesx = 0
        self.coordinatesy = 1000

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


class ballAnimate(turtle.Turtle):

    def __init__(self):

        turtle.Turtle.__init__(self)

        turtle.setworldcoordinates(0, 0, 5000, 5000)
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.goto(2500, 4900)
        self.showturtle()

    def movement(self, newX, newY):

        self.goto(newX, newY)


def directorAlgorithmX(angle, velMag):

    # The director algorithm X takes in an angle and a velocity to figure out the X vector component.

    xComponent = cos(angle) * velMag
    xComponent = round(xComponent)

    return xComponent


def directorAlgorithmY(angle, velMag):

    # The director algorithm Y takes in an angle and a velocity to figure out the Y vector component.

    yComponent = sin(angle) * velMag
    yComponent = round(yComponent)
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


# partway through coding movingBall, I realized that this algorithm will fit better in a "while" loop for the animation of the
# physics sim. Regardless, I am keeping movingBall() as a reference point since it is my current best representation for what
# The simulation will look like!

def movingBall(initialA, initialV):

    # Algorithm for moving ball

    # SECOND 0

    # Initial angle set

    angle = initialA

    # Initial velocity set

    velocity = initialV

    # Calculate next X position

    currentX = ball.getCoordinatesx()
    movementX = directorAlgorithmX(angle, velocity)

    currentX = currentX + movementX

    ball.setCoordinatesx(currentX)

    # Calculate next Y position

    currentY = ball.getCoordinatesy()
    movementY = directorAlgorithmY(angle, velocity)

    currentY = currentY + movementY

    ball.setCoordinatesy(currentY)

    # edit the balls coordinates to reflect this change

    ball.setCoordinates(currentX, currentY)

    ballA.movement(currentX, currentY)
    # Calculate next velocity (Magnitude)

    velocity = velocityDelta(velocity, angle, -9.8)

    # Calculate next angle

    time.sleep(1)
    # SECOND 1


def velocityFunction(initialV, timeInput):

    # This is the updated position function, taking time into account.
    acceleration = -9.8
    velocity = initialV + timeInput * acceleration

    return velocity


def positionAlgorithm(initialV, position, time):

    # Start of algorithm
    # Determine velocity , which determines change in position
    # Change the position according to this

    positionChange = velocityFunction(initialV, time)
    print("Position Change = ", positionChange)
    position = position + positionChange
    return position


def main():

    # Ball color is a variable that will be changeable later

    ball = ballObject()
    ballCoordinatesx = ball.getCoordinatesx()
    ballCoordinatesy = ball.getCoordinatesy()

    # This is where the new turtle based code will go

    # Here we create the screen and add a title
    wn = turtle.Screen()
    wn.title("BouncyBall.py")
    wn.bgcolor("white")
    ballA = ballAnimate()

    t = 0
    yChange = 0
    initialV = 0
    yPosition = 4900
    frameTime = 1
    ballA.speed(0)
    # This is the beginning of the loop

    while t < 100:

        yChange = positionAlgorithm(initialV, yPosition, t)
        print("yChange = ", yChange)

        # After the position algorithm is worked out, the velocity needs to be iterated
        initialV = velocityFunction(initialV, t)

        yChange = round(yChange)

        ballA.goto(2500, yChange)
        t = t + frameTime
        time.sleep(1/37)

    print("Main Loop")
    wn.mainloop()


main()
