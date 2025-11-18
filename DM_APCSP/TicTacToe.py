import turtle

GS = turtle.Turtle()
Screen = GS.screen

Screen.tracer(0)
Screen.bgcolor((1,1,1))

GS.speed(0)
GS.ht()
GS.width(4)

AmountOfSquare = 5

def MainDraw(From, Amount):
    GS.penup()
    GS.setpos(From[0], From[1])
    GS.pendown()
    GS.forward(Amount)
    GS.penup()

def MainDrawTo(From, To):
    GS.penup()
    GS.setpos(From[0], From[1])
    GS.pendown()
    GS.setpos(To[0], To[1])
    GS.penup()

def InitializeBoard():
    global Drawing
    Drawing = True
    for i in range(AmountOfSquare-1):
        MainDrawTo((-150-(75*(AmountOfSquare-3))+(150*0),-100-(50*(AmountOfSquare-3))+(100*i)+50), (-150-(75*(AmountOfSquare-3))+(150*(AmountOfSquare-1)),-100-(50*(AmountOfSquare-3))+(100*i)+50))
        #MainDrawTo((-150,-50), (150,-50))
        #MainDrawTo((50,150), (50,-150))
        #MainDrawTo((-50,150), (-50,-150))
    Drawing = False


InitializeBoard()

CO = turtle.Turtle()
CO.speed(0)
CO.penup()
CO.seth(90)
CO.shape('square')
CO.width(4)

Drawing = False

PlayerMode = "Player"
Player = 1

CurrentTileX = 1
CurrentTileY = 1


OccupiedSpots = []

def DrawTextWinner(Winner):
    GS.penup()
    GS.teleport(0, 200)
    GS.pendown()
    GS.write(F"{Winner} has Won!", align="center" ,font=("Arial", 40, "bold"))

def DrawCross(Position):
    global OccupiedSpots
    global CurrentTileX
    global CurrentTileY
    global Player
    if not (CurrentTileX,CurrentTileY) in OccupiedSpots:
        OccupiedSpots.append({"Pos":(CurrentTileX,CurrentTileY), "Owner": "X"})
        #print(True)
        global Drawing
        Drawing = True
        CO.setpos(Position[0]-48, Position[1]-48)
        CO.seth(45)
        CO.pendown()
        CO.setpos(Position[0]+48, Position[1]+48)
        CO.penup()
        CO.setpos(Position[0]-48, Position[1]+48)
        CO.seth(-45)
        CO.pendown()
        CO.setpos(Position[0]+48, Position[1]-48)
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
        #print(True)
        global Drawing
        Drawing = True
        CO.setpos(Position[0], Position[1]-48)
        CO.seth(0)
        CO.pendown()
        CO.circle(48)
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
        return Check1L
    elif Check1R == Check2L and Check2L == Check3R:
        return Check1R
    #for i in range

def CheckAcross(Type):
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
                if Type == "Vertical":
                    if f"({k}, {j})" == str(i["Pos"]):
                        Check[k][str(j)] = i["Owner"]
                elif Type == "Horizontal":
                    if f"({j}, {k})" == str(i["Pos"]):
                        Check[k][str(j)] = i["Owner"]
    
    for i in Check:
        if i["0"] == i["1"] and i["1"] == i["2"]:
            return i["0"]


def Loop():
    global Drawing
    global CurrentTileX
    global CurrentTileY
    global OccupiedSpots
    if Drawing == False:
        CO.setpos(-100-(50*(AmountOfSquare-3))+(100*CurrentTileX),-100-(50*(AmountOfSquare-3))+(100*CurrentTileY))

    if Player == 1:
        CO.shape('square')
    if Player == 2:
        CO.shape('triangle')

    if Drawing == False:
        Screen.update()

    #print(OccupiedSpots)
    Winner = None
    TempDia = CheckDia()
    TempVert = CheckAcross("Vertical")
    TempHoriz = CheckAcross("Horizontal")
    if TempDia != None:
        Winner = TempDia
    if TempVert != None:
        Winner = TempVert
    if TempHoriz != None:
        Winner = TempHoriz

    if Winner != None:
        Drawing = False
        DrawTextWinner(Winner)


    Screen.ontimer(Loop, 10)

def moveRight():
    global CurrentTileX
    global AmountOfSquare
    if CurrentTileX < AmountOfSquare-1:
        CurrentTileX += 1

def moveLeft():
    global CurrentTileX
    if CurrentTileX > 0:
        CurrentTileX -= 1

def moveUp():
    global CurrentTileY
    global AmountOfSquare
    if CurrentTileY < AmountOfSquare-1:
        CurrentTileY += 1

def moveDown():
    global CurrentTileY
    if CurrentTileY > 0:
        CurrentTileY -= 1

def SelectPos():
    global Player
    global OccupiedSpots
    check = False
    for i in OccupiedSpots:
        #print(i["Pos"])
        if f"({CurrentTileX}, {CurrentTileY})" == str(i["Pos"]):
            check = True

    if check == False:
        if Player == 1:
            DrawCross((-100-(50*(AmountOfSquare-3))+(100*CurrentTileX),-100-(50*(AmountOfSquare-3))+(100*CurrentTileY)))
        else:
            DrawCircle((-100-(50*(AmountOfSquare-3))+(100*CurrentTileX),-100-(50*(AmountOfSquare-3))+(100*CurrentTileY)))

def ResetBoard():
    global OccupiedSpots
    global Player
    OccupiedSpots = []
    Player = 1
    GS.clear()
    CO.clear()
    InitializeBoard()


Screen.onkeypress(moveRight, "d")
Screen.onkeypress(moveLeft, "a")
Screen.onkeypress(moveUp, "w")
Screen.onkeypress(moveDown, "s")

Screen.onkeypress(SelectPos, "Return")

Screen.onkeypress(ResetBoard, "r")

Screen.listen()
Loop()
Screen.mainloop()