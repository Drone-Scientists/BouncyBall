# BouncyBall3_TheRefactoring.py
# This program is the third iteration of BouncyBall, using the built in graphics libraries instead of
# turtle.

from graphics import *
import math
import time


class ballInformation():

    def __init__(self):

        # speed information
        self.speedX = 0
        self.speedY = 10
        self.velocityX = 0
        self.velocityY = 0
        self.acceleration = -9.8

        self.radius = 10
        self.color = "blue"

        self.positionX = 375
        self.positionY = 500


def angleFinder(velocityX, velocityY):

    angle = math.atan(velocityY / velocityX)
    return angle


def deltaDistance(speed, time):

    # This function uses the speed unit vector to determine how far the ball travels in a direction.

    deltaD = speed * time
    return deltaD


def deltaSpeed(velocity, time):

    # This function uses velocity, acceleration, and time to figure out the change in speed

    deltaS = velocity * time
    return deltaS


def deltaVelocityY(velocityY, acceleration):

    # This function uses velocity, acceleration, and time to figure out the change in velocity.

    deltaVY = velocityY + acceleration
    return deltaVY


def deltaVelocityX(velocityX):

    deltaVX = velocityX * .5
    if deltaVX < 1:

        deltaVX = 0

    return deltaVX


def velocityLoss(velocity):

    # This function returns a velocity that is 25 percent less than the input velocity.

    velocity = velocity * -.75
    return velocity

# These next 6 functions adjust the ball graphic object to where it needs to go.


def afterCollisionAdjusterY(ballInformation, ballGraphic):

    ballCenter = ballGraphic.getCenter()
    ballY = ballCenter.getY()
    difference = ballInformation.radius - ballY
    ballGraphic.move(0, difference)


def afterCollisionAdjusterYLargerEnd(ballInformation, ballGraphic, largerEndY):

    ballCenter = ballGraphic.getCenter()
    ballY = ballCenter.getY()
    endAdjust = largerEndY - ballInformation.radius
    difference = endAdjust - ballY
    ballGraphic.move(0, difference)


def afterCollisionAdjusterX(ballInformation, ballGraphic):

    ballCenter = ballGraphic.getCenter()
    ballX = ballCenter.getX()
    difference = ballInformation.radius - ballX
    ballGraphic.move(difference, 0)


def afterCollisionAdjusterXLargerEnd(ballInformation, ballGraphic, largerEndX):

    ballCenter = ballGraphic.getcenter()
    ballX = ballCenter.getX()
    endAdjust = largerEndX - ballInformation.radius
    difference = endAdjust - ballX
    ballGraphic.move(0, difference)


def afterCollisionAdjusterCorner(ballInformation, ballGraphic):

    ballCenter = ballGraphic.getcenter()
    ballX = ballCenter.getX()
    ballY = ballCenter.getY()
    differenceY = ballInformation.radius - ballX
    differenceX = ballInformation.radius - ballY
    ballGraphic.move(differenceX, differenceY)


def afterCollisionAdjusterCornerLargerEnd(ballInformation, ballGraphic, largerEndX, largerEndY):

    ballCenter = ballGraphic.getcenter()
    ballX = ballCenter.getX()
    ballY = ballCenter.getY()
    endAdjustX = largerEndX - ballInformation.radius
    endAdjustY = largerEndY - ballInformation.radius
    differenceX = endAdjustX - ballX
    differenceY = endAdjustY - ballY
    ballGraphic.move(differenceX, differenceY)


def collisionDetector(ballInformation, window, ballGraphic):

    # this function detects collisions.

    ballCollision = False
    largerEndX = window.getWidth() - ballInformation.radius
    largerEndY = window.getHeight() - ballInformation.radius

    print("Window dimensions | LargerEndX : ",
          largerEndX, " largerEndY: ", largerEndY)

    if ballInformation.positionY < ballInformation.radius:

        # Set the ball's position in the information and the graphic to 1 ball distance away from the edge of window

        ballInformation.positionY = ballInformation.radius
        afterCollisionAdjusterY(ballInformation, ballGraphic)
        ballCollision = True

    if ballInformation.positionY > largerEndY:

        ballInformation.positionY = largerEndY
        afterCollisionAdjusterYLargerEnd(
            ballInformation, ballGraphic, largerEndY)
        ballCollision = True

    if ballInformation.positionX < ballInformation.radius:

        ballInformation.positionX = ballInformation.radius
        afterCollisionAdjusterX(ballInformation, ballGraphic)
        ballCollision = True

    if ballInformation.positionX > largerEndX:

        ballInformation.positionX = largerEndX
        afterCollisionAdjusterXLargerEnd(
            ballInformation, ballGraphic, largerEndX)
        ballCollision = True

    if ballInformation.positionX < ballInformation.radius and ballInformation.positionY < ballInformation.radius:

        ballInformation.positionX = ballInformation.radius
        ballInformation.positionY = ballInformation.radius
        afterCollisionAdjusterCorner(ballInformation, ballGraphic)
        ballCollision = True

    if ballInformation.positionX > largerEndX and ballInformation.positionY > largerEndY:

        ballInformation.positionX = largerEndX
        ballInformation.positionY = largerEndY
        afterCollisionAdjusterCornerLargerEnd(
            ballInformation, ballGraphic, largerEndX, largerEndY)
        ballCollision = True

    print("Collision = ", ballCollision)
    return ballCollision


def collisionDealer(ballInformation):

    # This function deals with collisions

    ballInformation.velocityY = velocityLoss(ballInformation.velocityY)
    ballInformation.velocityX = velocityLoss(ballInformation.velocityX)
    print("Collision Dealer called")


def updateBallState(ballInformation, window, ballGraphic, time):

    # This is where the update ball state algorithm will go.

    # Use the current ball information to figure out the change in X and/or Y values

    ballXD = deltaDistance(ballInformation.velocityX, time)
    ballYD = deltaDistance(ballInformation.velocityY, time)

    # check for collisions and deal with them.

    collision = False
    collision = collisionDetector(ballInformation, window, ballGraphic)

    if collision == True:

        collisionDealer(ballInformation)
        ballXD = deltaDistance(ballInformation.velocityX, time)
        ballYD = deltaDistance(ballInformation.velocityY, time)

    print("The balls Y delta is: ", ballYD)
    ballInformation.positionX = ballInformation.positionX + ballXD
    ballInformation.positionY = ballInformation.positionY + ballYD

    # move the ball in ballGraphic to match the new ballInformation
    # Moving the ball here is fairly complicated but basically you subtract the graphics coordinates from
    # the informations coordinates and move the ball the difference.

    ballPosition = ballGraphic.getCenter()
    ballX = ballPosition.getX()
    ballY = ballPosition.getY()

    ballXD = ballInformation.positionX - ballX
    ballYD = ballInformation.positionY - ballY

    ballGraphic.move(ballXD, ballYD)
    print("ball moved! : ", time)
    print("X Delta : ", ballXD, " | Y Delta : ", ballYD)

    velocityX = ballInformation.velocityX
    velocityY = ballInformation.velocityY
    positionX = ballInformation.positionX
    positionY = ballInformation.positionY

    # use the deltaVelocity functin to find the new velocity and set it

    ballInformation.velocityY = deltaVelocityY(
        velocityY, ballInformation.acceleration)
    ballInformation.velocityX = deltaVelocityX(velocityX)

    print("Velocity X: ", velocityX)
    print("Velocity Y: ", velocityY)
    print("Position X: ", positionX, " Position Y: ", positionY)


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

    print("Initial Position: ", BB.positionX, " , ", BB.positionY)
    # initialize time
    t = 0

    while t < 10:

        updateBallState(BB, wn, ball, t)
        time.sleep(1)
        t = t + 1
        print(t)

    keyPress = wn.getKey()


main()
