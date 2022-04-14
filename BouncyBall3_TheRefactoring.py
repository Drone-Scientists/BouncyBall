# BouncyBall3_TheRefactoring.py
# This program is the third iteration of BouncyBall, using the built in graphics libraries instead of
# turtle.

from graphics import *


class ballInformation():

    def __init__(self):

        # speed information
        self.speed = 10
        self.velocity = 0
        self.acceleration = -9.8

        self.radius = 10
        self.color = "blue"

        self.positionX = 375
        self.positionY = 500


def deltaSpeed(velocity, acceleration, time):

    deltaX = velocity * time + (1/2 * acceleration * time**2)
    return deltaX


def deltaVelocity(velocity, acceleration, time):

    deltaV = velocity + acceleration*time
    return deltaV


def updateBallState(ballInformation, window, ballGraphic):

    # This is where the update ball state algorithm will go.

    # Use the current ball information to figure out the change in Y values

    # check for collisions and deal with them.

    # use the deltaVelocity functin to find the new velocity
    pass


def main():

    # Setting up the window and coordinate systems
    wn = GraphWin("BouncyBall3_TheRefactoring.py", 750, 750)
    wn.setCoords(0, 0, 750, 750)

    # Creating the ball object
    BB = ballInformation()
    pt = Point(BB.positionX, BB.positionY)
    ball = Circle(pt, 10)
    ball.setFill("blue")
    ball.draw(wn)

    # initialize time
    t = 0

    keyPress = wn.getKey()


main()
