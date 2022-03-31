
# This is the second bouncyball program, it is meant to be the forge for the new improved version
# After the second version here is complete, it will be transferred over to the original.

# put the imports here

from math import *
import unittest
import turtle
import time


# This is the refined ballObject class to not be so cluttered.
# It also has more relevant information AND a starting angle!

class ballObject():

    def __init__(self):

        self.radius = 10
        self.positionX = 0
        self.positionY = 1000
        # angle is in degrees
        self.angle = -90
        self.velocity = 0
        self.acceleration = -9.8

    def setPositionY(self, positionX):

        self.positionX = positionX

    def setPositionY(self, positionY):

        self.positionY = positionY

    def setVelocity(self, velocity):

        self.velocity = velocity

    def setAngle(self, angle):

        self.angle = angle


# This function determines the velocity magnitude
# I think that This needs tweaking


def velocityFunction(initialV, timeInput):

    # This is the updated position function, taking time into account.
    acceleration = -9.8
    velocity = initialV + timeInput * acceleration

    return velocity


# Add the directorX and directorY functions here

def directorX(angle, velMag):

    # The director algorithm X takes in an angle and a velocity to figure out the X vector component.

    xComponent = cos(angle) * velMag

    return xComponent


def directorY(angle, velMag):

    # The director algorithm Y takes in an angle and a velocity to figure out the Y vector component.

    yComponent = sin(angle) * velMag

    return yComponent


# outline for bouncy ball algorithm

# updateBallState(ballObject)

    # The ballObject is passed into the function.

    # New X and Y coordinates are determined by the director functions

    # Check for collision with 4 if statements

    # Add the new X and Y components to the current coordinates.

    # Determine the next velocity using the velocity function. Change the velocity inside the ballObject

    #

def main():

    # Creating the ball object

    ball = ballObject()

    xCoord = ball.positionX
    yCoord = ball.positionY
