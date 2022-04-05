
# This is the second bouncyball program, it is meant to be the forge for the new improved version
# After the second version here is complete, it will be transferred over to the original.

# put the imports here

from math import *
import unittest
import turtle
import time


# This is the refined ballObject class to not be so cluttered.
# It also has more relevant information AND a starting angle!

class testingSuite(unittest.TestCase):

    # This is a black-box acceptance test, because it only cares about the input and output.

    def testVelocityFunctionZero(self):

        # This blackbox test shows the velocity with initialV being 0 and 5 seconds passing.
        self.assertEquals(velocityFunction(0, 5), (-49))

    def testVelocityFunctionRecursive(self):

        self.assertEquals(velocityFunction(-49, 5), (-98))

        # This blackbox test takes the output from the previous test

    # These next tests are white-box acceptance tests, with full branch coverage

    # exitAngler code included below for the test

    # def exitAngler(angle,  wall):

    # This function is called when a ball is bouncing.

    # group of if statements for different walls - calculating exit angles
    # these calculations assume the ball has a perfect reflective bounce.

    # if wall == "bottom":

        #bounceAngle = 180 - angle

    # if wall == "top":

        #bounceAngle = 540 - angle

    # if wall == "left":

        # if angle < 90:

        #bounceAngle = angle + 270

        # if angle > 270:

        #bounceAngle = angle - 270

    # if wall == "right":

        # if angle < 180:

        #bounceAngle = angle + 90

        # if angle > 180:

        #bounceAngle = angle - 90

    # return bounceAngle

    def testExitAnglerBottom(self):

        # Bottom branch coverage
        self.assertEquals(exitAngler(45, "bottom"), 135)

    def textExitAnglerTop(self):

        # Top branch coverage
        self.assertEquals(exitAngler(45, "top"), 495)

    def testExitAnglerLeftLessThan(self):

        # Left less than 90 branch coverage
        self.assertEquals(exitAngler(45, "left"), 315)

    def testExitAnglerLeftMoreThan(self):

        # Left more than 90 branch coverage
        self.assertEquals(exitAngler(135, "left"), -135)

    def testExitAnglerRightLessThan(self):

        # Right less than 180 branch coverage

        self.assertEquals(exitAngler(45, "right"), 135)

    def textExitAnglerRightMoreThan(self):

        # Right more than 180 branch coverage

        self.assertEquals(exitAngler(225, "right"), 135)


class ballObject():

    def __init__(self):

        self.radius = 10

        self.positionX = 750

        self.positionY = 1000

        # angle is in degrees
        self.angle = -90

        self.velocity = 0

        # acceleration tuple (x, y)
        self.acceleration = (0, -9.8)

    def setPositionX(self, positionX):

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


def exitAngler(angle,  wall):

    # This function is called when a ball is bouncing.

    # group of if statements for different walls - calculating exit angles
    # these calculations assume the ball has a perfect reflective bounce.

    if wall == "bottom":

        bounceAngle = 180 - angle

    if wall == "top":

        bounceAngle = 540 - angle

    if wall == "left":

        if angle < 90:

            bounceAngle = angle + 270

        if angle > 270:

            bounceAngle = angle - 270

    if wall == "right":

        if angle < 180:

            bounceAngle = angle + 90

        if angle > 180:

            bounceAngle = angle - 90

    return bounceAngle


def ballVelocityLoss(vMag):

    # What we need: Velocity Magnitude

    KE = 1/2 * (vMag) ^ 2

    # For this simulation, we are assuming that the ball loses 25 percent of its velocity when it collides
    # with the ground.

    vMag = vMag * .75
    if vMag < 0:
        vMag = vMag * -1

    return vMag


def updateBallState(ballObject):

    # The ballObject is passed into the function.
    # New X and Y unit vectors are determined by the director functions

    xVector = directorX(ballObject.angle, ballObject.velocity)
    yVector = directorY(ballObject.angle, ballObject.velocity)

    # Check for collision with 4 if statements

    if (ballObject.positionY + yVector) < 10:

        # bounce up

        ballObject.positionY = 10
        ballObject.angle = exitAngler(ballObject.angle, "bottom")
        ballObject.velocity = ballVelocityLoss(ballObject.velocity)

    if (ballObject.positionY + yVector) < 1490:

        # bounce down

        ballObject.positionY = 1490
        ballObject.angle = exitAngler(ballObject.angle, "top")
        ballObject.velocity = ballVelocityLoss(ballObject.velocity)

        if ballObject.velocity > 0:

            ballObject.velocity = ballObject.velocity * -1

    if (ballObject.positionX + xVector) < 10:

        # bounce Right
        ballObject.positionX = 10
        ballObject.angle = exitAngler(ballObject.angle, "left")
        ballObject.velocity = ballVelocityLoss(ballObject.velocity)

    # Add the new X and Y components to the current coordinates.

    # Determine the next velocity using the velocity function. Change the velocity inside the ballObject

    #


def main():

    # Creating the ball object

    ball = ballObject()

    xCoord = ball.positionX
    yCoord = ball.positionY

    wn = turtle.Screen()
    wn.bgcolor = "white"
    wn.title("BouncyBall.py")
    wn.setworldcoordinates(-1, -1, 1500, 1500)

    BB = turtle.Turtle()
    BB.shape("circle")
    BB.color("blue")
    BB.penup()
    BB.speed(0)
    BB.goto(ball.positionX, ball.positionY)

    print("Main Loop")
    wn.mainloop()


main()
