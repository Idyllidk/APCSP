import turtle
#import asyncio

global FLIGHTMODE
FLIGHTMODE = False

GS = turtle.Turtle()
Screen = GS.getscreen()

GS.forward(1)
GS.speed(0)
GS.penup()
GS.seth(90)
GS.color("red")

PLATFORM_HEIGHT = -50
PLATFORM_WIDTH = 350
PLATFORM_START = -175

WD = turtle.Turtle()
WD.speed(0)
WD.penup()
WD.width(10)
WD.fillcolor((0,0,0))
WD.color((0,0,0))

Screen.tracer(0)
Screen.bgcolor((1,1,1))

print(Screen.turtles())
#print("Gravity/Collision Test.")

"""
Platform Setup
1: Platform Start
2: Platform Width
3: Platform Height
"""

Platforms = {
  "MainPlatform": [
    -175,
    350,
    -75,
    10
  ],
  "Platform2": [
    225,
    40,
    -65,
    3
  ],
  "Platform22": [
    -265,
    40,
    -65,
    3
  ],
  "Platform3": [
    -100,
    200,
    -25,
    7
  ],
  "Platform4": [
    -75,
    150,
    65,
    5
  ],
}

for item, Platform in Platforms.items():
  #WD.setx(Platform[0])
  #WD.sety(Platform[2])
  #WD.pendown()
  #WD.forward(Platform[1])
  #WD.penup()
  for i in range(Platform[3]):
      WD.setx(Platform[0]+(i*5))
      WD.sety(Platform[2]+(i*3))
      WD.pendown()
      WD.forward(Platform[1]-(i*10))
      WD.penup()

WD.hideturtle()

global CanJump
global Direction
global MovingLeft
global MovingRight
global FallingSpeed
global Jumping
global tempCollisionType
global checked
CanJump = True
Direction = 0
MovingLeft = False
MovingRight = False
FallingSpeed = 0
Jumping = False
tempCollisionType = "None"
checked = False

def CheckTouching(offset = 0, xoffset = 0):
  tempValue = False
  for item, Plat in Platforms.items():
    if (
       (GS.ycor()+offset < Plat[2]+(5*Plat[3]/2) and 
        GS.ycor()+offset > Plat[2]-5) and
       (GS.xcor() <= (Plat[0]+Plat[1]+3-xoffset) and 
        GS.xcor() >= Plat[0]-3+xoffset)):
      return True
  if GS.ycor()+offset < -150:
    return True
  return False  

#CheckTouching()

def Gravity():
  if CanFall == True:
    CanFall = False
    if CheckTouching():
      while CheckTouching():
        FallingSpeed = FallingSpeed - 0.5
    CanJump = True

def actualJump():
  global CanJump
  global FallingSpeed
  global Jumping
  if CanJump == True and Jumping == True:
    Jumping = True
    theoreticalSpeed = FallingSpeed
    if theoreticalSpeed < 1:
      theoreticalSpeed = 1
    if theoreticalSpeed <= 10:
      FallingSpeed = FallingSpeed + (7.5/int(theoreticalSpeed))
    elif FLIGHTMODE == False:
      CanJump = False

def jump():
  global Jumping
  Jumping = True

def endJump():
  global CanJump
  global Jumping
  global FallingSpeed
  global FLIGHTMODE
  Jumping = False
  if FLIGHTMODE == True:
    FallingSpeed = 0
  elif FLIGHTMODE == False:
    CanJump = False

def flyDown():
  global FLIGHTMODE
  global FallingSpeed
  if FLIGHTMODE == True:
    FallingSpeed = -7.5

def flyDownEnd():
  global FLIGHTMODE
  global FallingSpeed
  if FLIGHTMODE == True:
    FallingSpeed = 0

def Loop():
    TheoreticalStop = False
    global Direction
    global MovingLeft
    global MovingRight
    global FallingSpeed
    global CanJump
    global tempCollisionType
    global checked

    if MovingRight == True and MovingLeft == True:
      Direction = 0
    elif MovingLeft == True:
      Direction = -1
    elif MovingRight == True:
      Direction = 1
    else:
      Direction = 0

    GS.speed(0)
    actualJump()
    #print(tempCollisionType)

    if FLIGHTMODE == False:
      if not CheckTouching():
        if Jumping == False:
          CanJump = False
          checked = False
        FallingSpeed -= 0.5
      elif CheckTouching() and FallingSpeed <= 0 and tempCollisionType != "Top":
        FallingSpeed = 0
        CanJump = True
      elif CheckTouching() and tempCollisionType != "Bottom":
        FallingSpeed -= 0.5

      #print(CheckTouching(), FallingSpeed, tempCollisionType)

    '''
    if not CheckTouching():
        tempCollisionType = "None"
        FallingSpeed -= 0.5
    elif (CheckTouching() and tempCollisionType == "Top" and tempCollisionType != "Bottom"):
       tempCollisionType = "None"
       FallingSpeed = 0
       FallingSpeed -= 0.5
    elif CheckTouching() and FallingSpeed <= 0:
       tempCollisionType = "Bottom"
       FallingSpeed = 0
       CanJump = True
    elif CheckTouching(0.5) and FallingSpeed > 0 and tempCollisionType == "None":
       tempCollisionType = "Top"
       FallingSpeed = 0
    '''
    
    #if CheckTouching(.5):
        #GS.sety(GS.ycor() + .5)

    #if checked == False:
    if FallingSpeed < 0 and not CheckTouching():
      tempCollisionType = "Bottom"
      tempFallingSpeed = FallingSpeed
      for i in range(int(-tempFallingSpeed)):
        if CheckTouching(FallingSpeed-i) and tempCollisionType != "Top":
            FallingSpeed += 1
            #Direction = 0
            if FLIGHTMODE == False:
              CanJump = True
    elif FallingSpeed > 0:
      tempCollisionType = "Top"
      tempFallingSpeed = FallingSpeed
      for i in range(int(tempFallingSpeed)):
        if CheckTouching(FallingSpeed-i):
            if FLIGHTMODE == False:
              CanJump = False
            FallingSpeed -= 1
    
    if CheckTouching(0.1) and FallingSpeed == 0:
       while CheckTouching(0.1):
          GS.sety(GS.ycor()+0.1)
      #checked = True

    #print(Depth)

    #if FallingSpeed != 0:
    GS.setx(GS.xcor() + (Direction*5))
    GS.sety(GS.ycor() + FallingSpeed)

    Screen.update()

    Screen.ontimer(Loop, 10)

def moveLeft():
    global MovingLeft
    MovingLeft = True

def endLeft():
    global MovingLeft
    MovingLeft = False

def moveRight():
    global MovingRight
    MovingRight = True

def endRight():
    global MovingRight
    MovingRight = False

Screen.onkeypress(moveLeft, "a")
Screen.onkeypress(moveRight, "d")
#Screen.onkeypress(moveForward, "e")
#Screen.onkeypress(moveBackward, "q")
Screen.onkeyrelease(endLeft, "a")
Screen.onkeyrelease(endRight, "d")
#Screen.onkeyrelease(endForward, "e")
#Screen.onkeyrelease(endBackward, "q")
Screen.onkeypress(jump, "w")
Screen.onkeyrelease(endJump, "w")

Screen.onkeypress(flyDown, "s")
Screen.onkeyrelease(flyDownEnd, "s")

Screen.listen()
Loop()
Screen.mainloop()