# BouncyBall3_TheRefactoring.py
# This program is the third iteration of BouncyBall, using the built in graphics libraries instead of
# turtle.

from graphics import *
import math
import time


class ballInformation():

    def __init__(self):

        # speed information

        self.positionX = 375
        self.positionY = 500
        self.speedX = 0
        self.speedY = -10
        self.collisionX = self.positionX
        self.collisionY = self.positionY
        self.velocityX = 0
        self.velocityY = 0
        self.acceleration = -9.8

        self.radius = 10
        self.color = "blue"


def angleFinder(velocityX, velocityY):

    angle = math.atan(velocityY / velocityX)
    return angle


def deltaDistance(speed):

    # This function uses the speed unit vector to determine how far the ball travels in a direction.

    deltaD = 0
    deltaD = deltaD + speed
    return deltaD


def deltaSpeed(velocity):

    # This function uses velocity, acceleration, and time to figure out the change in speed

    deltaS = 0
    deltaS = deltaS + velocity
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

    velocity = velocity * -.25
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

    if ballInformation.collisionY < ballInformation.radius:

        # Set the ball's position in the information and the graphic to 1 ball distance away from the edge of window

        ballInformation.positionY = ballInformation.radius
        afterCollisionAdjusterY(ballInformation, ballGraphic)
        ballInformation.collisionY = ballInformation.positionY
        ballCollision = True

    if ballInformation.collisionY > largerEndY:

        ballInformation.positionY = largerEndY
        afterCollisionAdjusterYLargerEnd(
            ballInformation, ballGraphic, largerEndY)
        ballInformation.collisionY = ballInformation.positionY
        ballCollision = True

    if ballInformation.collisionX < ballInformation.radius:

        ballInformation.positionX = ballInformation.radius
        afterCollisionAdjusterX(ballInformation, ballGraphic)
        ballInformation.collisionX = ballInformation.positionX
        ballCollision = True

    if ballInformation.collisionX > largerEndX:

        ballInformation.positionX = largerEndX
        afterCollisionAdjusterXLargerEnd(
            ballInformation, ballGraphic, largerEndX)
        ballInformation.collisionX = ballInformation.positionX
        ballCollision = True

    if ballInformation.collisionX < ballInformation.radius and ballInformation.collisionY < ballInformation.radius:

        ballInformation.positionX = ballInformation.radius
        ballInformation.positionY = ballInformation.radius
        afterCollisionAdjusterCorner(ballInformation, ballGraphic)
        ballInformation.collisionX = ballInformation.positionX
        ballInformation.collisionY = ballInformation.positionY
        ballCollision = True

    if ballInformation.collisionX > largerEndX and ballInformation.collisionY > largerEndY:

        ballInformation.positionX = largerEndX
        ballInformation.positionY = largerEndY
        afterCollisionAdjusterCornerLargerEnd(
            ballInformation, ballGraphic, largerEndX, largerEndY)
        ballInformation.collisionX = ballInformation.positionX
        ballInformation.collisionY = ballInformation.positionY
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

    BBXD = deltaDistance(ballInformation.speedX)
    BBYD = deltaDistance(ballInformation.speedY)
    PX = ballInformation.positionX
    PY = ballInformation.positionY
    ballInformation.collisionX = PX + BBXD
    ballInformation.collisionY = PY + BBYD
    collideX = ballInformation.collisionX
    collideY = ballInformation.collisionY

    print("collisionX = ", collideX, " | collisionY = ", collideY)

    # check for collisions and deal with them.

    collision = False
    collision = collisionDetector(ballInformation, window, ballGraphic)

    if collision == True:

        collisionDealer(ballInformation)
        BBSX = ballInformation.speedX
        BBSY = ballInformation.speedY
        ballInformation.speedX = BBSX * -1
        ballInformation.speedY = BBSY * -1
        BBXD = deltaDistance(ballInformation.speedX)
        BBYD = deltaDistance(ballInformation.speedY)

    print("The balls Y delta is: ", BBYD)
    ballInformation.positionX = ballInformation.positionX + BBXD
    ballInformation.positionY = ballInformation.positionY + BBYD

    # move the ball in ballGraphic to match the new ballInformation
    # Moving the ball here is fairly complicated but basically you subtract the graphics coordinates from
    # the informations coordinates and move the ball the difference.

    ballPosition = ballGraphic.getCenter()
    ballX = ballPosition.getX()
    ballY = ballPosition.getY()

    BBXD2 = ballInformation.positionX - ballX
    BBYD2 = ballInformation.positionY - ballY

    ballGraphic.move(BBXD2, BBYD2)
    print("ball moved! : ", time)
    print("X Delta : ", BBXD2, " | Y Delta : ", BBYD2)

    speedX = ballInformation.speedX
    speedY = ballInformation.speedY
    velocityX = ballInformation.velocityX
    velocityY = ballInformation.velocityY
    positionX = ballInformation.positionX
    positionY = ballInformation.positionY

    # Change the speed
    ballInformation.speedX = deltaSpeed(ballInformation.velocityX)
    ballInformation.speedY = deltaSpeed(ballInformation.velocityY)

    # Change the velocity
    ballInformation.velocityY = deltaVelocityY(
        velocityY, ballInformation.acceleration)
    ballInformation.velocityX = deltaVelocityX(velocityX)

    print("Speed X: ", speedX)
    print("Speed Y: ", speedY)
    print("Velocity X: ", velocityX)
    print("Velocity Y: ", velocityY)
    print("Position X: ", positionX, " Position Y: ", positionY)


def BBSim(ballInformation, ballGraphic, window, timeMax):

    t = 0
    while t < timeMax:

        updateBallState(ballInformation, window, ballGraphic, t)
        time.sleep(.5)
        t = t + 1
        print(t)

    keyPress = window.getKey()


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

    t = 50
    print("Initial Position: ", BB.positionX, " , ", BB.positionY)
    BBSim(BB, ball, wn, t)


main()
