import turtle

GS = turtle.Turtle()
Screen = GS.screen

Screen.tracer(0)
Screen.bgcolor((1,1,1))

GS.speed(0)
GS.ht()

def MainDraw(From, Amount):
    GS.penup()
    GS.setpos(From[0], From[1])
    GS.pendown()
    GS.forward(Amount)
    GS.penup()

def InitializeBoard():
    MainDraw((-150,50), 300)
    MainDraw((-150,-50), 300)
    GS.seth(-90)
    MainDraw((50,150), 300)
    MainDraw((-50,150), 300)


InitializeBoard()

CO = turtle.Turtle()
CO.speed(0)
CO.penup()
CO.seth(90)
CO.shape('square')

Drawing = False

PlayerMode = "Player"
Player = 1

CurrentTileX = 1
CurrentTileY = 1


OccupiedSpots = []

def DrawCross(Position):
    global OccupiedSpots
    global CurrentTileX
    global CurrentTileY
    global Player
    if not (CurrentTileX,CurrentTileY) in OccupiedSpots:
        OccupiedSpots.append({"Pos":(CurrentTileX,CurrentTileY), "Owner": "X"})
        print(True)
        global Drawing
        Drawing = True
        CO.setpos(Position[0]-50, Position[1]-50)
        CO.seth(45)
        CO.pendown()
        CO.forward(141.421)
        CO.penup()
        CO.setpos(Position[0]-50, Position[1]+50)
        CO.seth(-45)
        CO.pendown()
        CO.forward(141.421)
        CO.penup()
        CO.seth(90)
        Player = 2
        Drawing = False

def DrawCircle(Position):
    global OccupiedSpots
    global CurrentTileX
    global CurrentTileY
    global Player
    if not (CurrentTileX,CurrentTileY) in OccupiedSpots:
        OccupiedSpots.append({"Pos":(CurrentTileX,CurrentTileY), "Owner": "O"})
        print(True)
        global Drawing
        Drawing = True
        CO.setpos(Position[0], Position[1]-50)
        CO.seth(0)
        CO.pendown()
        CO.circle(50)
        CO.penup()
        CO.seth(90)
        Player = 1
        Drawing = False

def CheckDia():
    global OccupiedSpots
    Check1L = "1"
    Check2L = "2"
    Check3L = "3"
    Check1R = "4"
    Check3R = "5"
    for i in OccupiedSpots:
        if i["Pos"] == (0, 0):
            Check1L = i["Owner"]
        if i["Pos"] == (1, 1):
            Check2L = i["Owner"]
        if i["Pos"] == (2, 2):
            Check3L = i["Owner"]
        if i["Pos"] == (2, 0):
            Check1R = i["Owner"]
        if i["Pos"] == (0, 2):
            Check3R = i["Owner"]
    if Check1L == Check2L and Check2L == Check3L:
        print(Check1L)
    elif Check1R == Check2L and Check2L == Check3R:
        print(Check1R)

def is_descendant(item, nested_list):
    for element in nested_list:
        if element == item:
            return True
        elif isinstance(element, list) and is_descendant(item, element):
            return True
    return False

def CheckAcross():
    global OccupiedSpots
    Check = [
        {
            "0": "0",
            "1": "1",
            "2": "2"
        },
        {
            "0": "0",
            "1": "1",
            "2": "2"
        },
        {
            "0": "0",
            "1": "1",
            "2": "2"
        }
    ]
    for i in OccupiedSpots:
        for k in range(3):
            for j in range(3):
                if f"({k}, {j})" == str(i["Pos"]):
                    Check[k][str(j)] = i["Owner"]
    
    for i in Check:
        if i["0"] == i["1"] and i["1"] == i["2"]:
            print("Vert")
    '''if Check1L == Check2L and Check2L == Check3L:
        print(Check1L)
    elif Check1R == Check2L and Check2L == Check3R:
        print(Check1R)'''


def Loop():
    global Drawing
    global CurrentTileX
    global CurrentTileY
    global OccupiedSpots
    if Drawing == False:
        CO.setpos(-100+(100*CurrentTileX),-100+(100*CurrentTileY))

    if Player == 1:
        CO.shape('square')
    if Player == 2:
        CO.shape('triangle')

    if Drawing == False:
        Screen.update()

    #print(OccupiedSpots)
    CheckDia()
    CheckAcross()
    

    Screen.ontimer(Loop, 10)

def moveRight():
    global CurrentTileX
    if CurrentTileX < 2:
        CurrentTileX += 1

def moveLeft():
    global CurrentTileX
    if CurrentTileX > 0:
        CurrentTileX -= 1

def moveUp():
    global CurrentTileY
    if CurrentTileY < 2:
        CurrentTileY += 1

def moveDown():
    global CurrentTileY
    if CurrentTileY > 0:
        CurrentTileY -= 1

def SelectPos():
    global Player
    if Player == 1:
        DrawCross((-100+(100*CurrentTileX),-100+(100*CurrentTileY)))
    else:
        DrawCircle((-100+(100*CurrentTileX),-100+(100*CurrentTileY)))


Screen.onkeypress(moveRight, "d")
Screen.onkeypress(moveLeft, "a")
Screen.onkeypress(moveUp, "w")
Screen.onkeypress(moveDown, "s")

Screen.onkeypress(SelectPos, "Return")

Screen.listen()
Loop()
Screen.mainloop()