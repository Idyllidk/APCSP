import turtle

GS = turtle.Turtle()
Screen = GS.screen

Screen.tracer(0)
Screen.bgcolor((1,1,1))

GS.speed(0)
GS.ht()
GS.width(4)

AmountOfSquare = 3
#RECOMMENDED MAXIMUM IS 7 IN FULL SCREEN MODE
#DO NOT GO OVER 7 UNLESS YOU REALLY WANT TO

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
        MainDrawTo((-150-(50*(AmountOfSquare-3))+(150*0),-100-(50*(AmountOfSquare-3))+(100*i)+50), (-150-(100*(AmountOfSquare-3))+(150*(AmountOfSquare-1)),-100-(50*(AmountOfSquare-3))+(100*i)+50))
        MainDrawTo((-100-(50*(AmountOfSquare-3))+(100*i)+50, -150-(50*(AmountOfSquare-3))+(150*0)), ((-100-(50*(AmountOfSquare-3))+(100*i)+50), (-150-(100*(AmountOfSquare-3))+(150*(AmountOfSquare-1)))))
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

CurrentTileX = 0
CurrentTileY = 0

SizeOffset = -10

if AmountOfSquare == 1:
    CurrentTileX, CurrentTileY = 0, 0
elif AmountOfSquare % 2 != 0:
    CurrentTileX, CurrentTileY = (AmountOfSquare-1)//2, (AmountOfSquare-1)//2
else:
    CurrentTileX, CurrentTileY = 0, AmountOfSquare-1

print(CurrentTileX, CurrentTileY)

Won = False


OccupiedSpots = []

def DrawTextWinner(Winner):
    GS.penup()
    GS.teleport(0, 200+(50*(AmountOfSquare-3)))
    GS.pendown()
    GS.write(F"{Winner} has Won!", align="center" ,font=("Verdana", 40, "bold"))

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
        CO.setpos(Position[0]-(50+SizeOffset), Position[1]-(50+SizeOffset))
        CO.seth(45)
        CO.pendown()
        CO.setpos(Position[0]+(50+SizeOffset), Position[1]+(50+SizeOffset))
        CO.penup()
        CO.setpos(Position[0]-(50+SizeOffset), Position[1]+(50+SizeOffset))
        CO.seth(-45)
        CO.pendown()
        CO.setpos(Position[0]+(50+SizeOffset), Position[1]-(50+SizeOffset))
        CO.penup()
        CO.seth(90)
        Player = 2
        Drawing = False

def DrawCircle(Position):
    global OccupiedSpots
    global CurrentTileX
    global CurrentTileY
    global Player
    global SizeOffset
    if not (CurrentTileX,CurrentTileY) in OccupiedSpots:
        OccupiedSpots.append({"Pos":(CurrentTileX,CurrentTileY), "Owner": "O"})
        #print(True)
        global Drawing
        Drawing = True
        CO.setpos(Position[0], Position[1]-(50+SizeOffset))
        CO.seth(0)
        CO.pendown()
        CO.circle(50+SizeOffset)
        CO.penup()
        CO.seth(90)
        Player = 1
        Drawing = False

def CheckDia():
    global OccupiedSpots
    global AmountOfSquare
    Check = []

    for k in range(2):
        TempCheck = {}
        
        for j in range(AmountOfSquare):
            target_pos = ""
            if k == 0:
                target_pos = f"({j}, {j})"
            else:
                target_pos = f"({AmountOfSquare - 1 - j}, {j})"

            for i in OccupiedSpots:
                if str(i["Pos"]) == target_pos:
                    TempCheck[str(j)] = i["Owner"]

        if TempCheck:
            Check.append(TempCheck)

    for row_data in Check:
        if len(row_data) == AmountOfSquare:
            owners = list(row_data.values())
            first_owner = owners[0]
            if all(owner == first_owner for owner in owners):
                return first_owner

    return None

def CheckAcross(Type):
    global OccupiedSpots
    global AmountOfSquare
    Check = []

    for k in range(AmountOfSquare):
        TempCheck = {}
        
        for j in range(AmountOfSquare):
            target_pos = ""
            if Type == "Vertical":
                target_pos = f"({k}, {j})"
            elif Type == "Horizontal":
                target_pos = f"({j}, {k})"

            for i in OccupiedSpots:
                if str(i["Pos"]) == target_pos:
                    TempCheck[str(j)] = i["Owner"]

        if TempCheck:
            Check.append(TempCheck)

    for row_data in Check:
        if len(row_data) == AmountOfSquare:
            owners = list(row_data.values())
            
            first_owner = owners[0]
            if all(owner == first_owner for owner in owners):
                return first_owner

    return None


def Loop():
    global Drawing
    global CurrentTileX
    global CurrentTileY
    global OccupiedSpots
    global Won
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

    if Won == False:
        TempDia = CheckDia()
        TempVert = CheckAcross("Vertical")
        TempHoriz = CheckAcross("Horizontal")
        if TempDia != None:
            Winner = TempDia
        if TempVert != None:
            Winner = TempVert
        if TempHoriz != None:
            Winner = TempHoriz

    #print(Winner)
    if Winner != None:
        #Won = True
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
    global Won
    global OccupiedSpots
    global Player
    OccupiedSpots = []
    Player = 1
    GS.clear()
    CO.clear()
    InitializeBoard()
    Won = False


Screen.onkeypress(moveRight, "d")
Screen.onkeypress(moveLeft, "a")
Screen.onkeypress(moveUp, "w")
Screen.onkeypress(moveDown, "s")

Screen.onkeypress(SelectPos, "Return")

Screen.onkeypress(ResetBoard, "r")

Screen.listen()
Loop()
Screen.mainloop()