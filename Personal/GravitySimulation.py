import turtle

GS = turtle.Turtle()
Screen = turtle.getscreen()

GS.forward(1)
GS.speed(0)
GS.penup()
GS.seth(90)

PLATFORM_HEIGHT = -50
PLATFORM_WIDTH = 350
PLATFORM_START = -175

WD = turtle.Turtle()
WD.speed(0)
WD.penup()
WD.width(10)

Screen.tracer(0)

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
    -75     
  ],
  "Platform2": [
    225,
    40,
    -75   
  ],
  "Platform22": [
    -265,
    40,
    -75   
  ],
  "Platform3": [
    -100,
    200,
    -25  
  ],
  "Platform4": [
    -75,
    150,
    65    
  ],
}

for item, Platform in Platforms.items():
  WD.setx(Platform[0])
  WD.sety(Platform[2])
  WD.pendown()
  WD.forward(Platform[1])
  WD.penup()


global CanJump
global Direction
global MovingLeft
global MovingRight
global FallingSpeed
CanJump = True
Direction = 0
MovingLeft = False
MovingRight = False
FallingSpeed = 0

def CheckTouching():
  tempValue = False
  for item, Plat in Platforms.items():
    if ((GS.ycor() < Plat[2]+15 and GS.ycor() > Plat[2]-15) and (GS.xcor() <= (Plat[0]+Plat[1]) and GS.xcor() >= Plat[0])):
      return True
  if GS.ycor() < -150:
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

def jump():
  global CanJump
  global FallingSpeed
  if CanJump:
     FallingSpeed = 10
     CanJump = False

def Loop():
    global Direction
    global MovingLeft
    global MovingRight
    global FallingSpeed
    global CanJump

    if MovingRight == True and MovingLeft == True:
      Direction = 0
    elif MovingLeft == True:
      Direction = -1
    elif MovingRight == True:
      Direction = 1
    else:
      Direction = 0

    GS.speed(0)

    if not CheckTouching():
        FallingSpeed -= 0.5
    elif CheckTouching() and FallingSpeed <= 0:
       FallingSpeed = 0
       CanJump = True
    
    if CheckTouching():
        GS.sety(GS.ycor() + 1)

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
Screen.onkeyrelease(endLeft, "a")
Screen.onkeyrelease(endRight, "d")
Screen.onkey(jump, "w")

Screen.listen()
Loop()
Screen.mainloop()