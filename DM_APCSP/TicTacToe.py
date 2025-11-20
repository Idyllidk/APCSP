import turtle
import random

GS = turtle.Turtle()
Screen = GS.screen

Screen.tracer(0)
Screen.bgcolor((1,1,1))

GS.speed(0)
GS.ht()
GS.width(4)

AmountOfSquare = 3  #Change this number to change the size of the Tic Tac Toe board. Recommended max is 7.

#There are TWO player modes; Computer or Player.
PlayerMode = "Computer"
Player = 1

#If PlayerMode is set to Computer, the computer will play as O, There are 2 modes for the computer: "Random" and "Smart"
#If you want to feel good about yourself, you should probably pick "Random"
#Warning: "Smart" mode isn't completely smart and will replicate losses if you repeat the same moves.
ComputerMode = "Smart"

Score = {
    "X": 0,
    "O": 0
}

SB = turtle.Turtle()
SB.hideturtle()
SB.speed(0)
SB.penup()
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

def DrawTextScore():
    global Score
    SB.clear()
    SB.penup()
    SB.teleport(-150, 150+(50*(AmountOfSquare-3)))
    SB.pendown()
    SB.write(F"X: {Score['X']}", align="left" ,font=("Verdana", 32, "bold"))
    SB.penup()
    SB.teleport(150, 150+(50*(AmountOfSquare-3)))
    SB.pendown()
    SB.write(F"O: {Score['O']}", align="right" ,font=("Verdana", 32, "bold"))
DrawTextScore()

def DrawCross(Position):
    global OccupiedSpots
    global CurrentTileX
    global CurrentTileY
    global Player
    #print(CurrentTileX, CurrentTileY)
    #print(OccupiedSpots)
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

def DrawCircleManual(Position):
    global OccupiedSpots
    global Player
    global SizeOffset
    if not (Position[0],Position[1]) in OccupiedSpots:
        OccupiedSpots.append({"Pos":(Position[0],Position[1]), "Owner": "O"})
        #print(True)
        global Drawing
        Drawing = True
        CO.setpos((-100-(50*(AmountOfSquare-3))+(100*Position[0]),-100-(50*(AmountOfSquare-3))+(100*Position[1])-(50+SizeOffset)))
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

#EVERYTHING FROM HERE ON UNTIL THE END OF THE "ChooseAIMove" FUNCTION IS THE SMARTER AI CODE FOR COMPUTER PLAYER, EVERYTHING ELSE IS MINE AND WAS WRITTEN BEFOREHAND
def get_owner(x, y):
    for i in OccupiedSpots:
        if i["Pos"] == (x, y):
            return i["Owner"]
    return None

def find_winning_move(owner):
    # check rows
    for r in range(AmountOfSquare):
        count_owner = 0
        empty = None
        for c in range(AmountOfSquare):
            o = get_owner(c, r)
            if o == owner:
                count_owner += 1
            elif o is None:
                empty = (c, r)
        if count_owner == AmountOfSquare - 1 and empty is not None:
            return empty

    # check columns
    for c in range(AmountOfSquare):
        count_owner = 0
        empty = None
        for r in range(AmountOfSquare):
            o = get_owner(c, r)
            if o == owner:
                count_owner += 1
            elif o is None:
                empty = (c, r)
        if count_owner == AmountOfSquare - 1 and empty is not None:
            return empty

    # main diagonal
    count_owner = 0
    empty = None
    for i in range(AmountOfSquare):
        o = get_owner(i, i)
        if o == owner:
            count_owner += 1
        elif o is None:
            empty = (i, i)
    if count_owner == AmountOfSquare - 1 and empty is not None:
        return empty

    # anti-diagonal
    count_owner = 0
    empty = None
    for i in range(AmountOfSquare):
        o = get_owner(AmountOfSquare - 1 - i, i)
        if o == owner:
            count_owner += 1
        elif o is None:
            empty = (AmountOfSquare - 1 - i, i)
    if count_owner == AmountOfSquare - 1 and empty is not None:
        return empty

    return None

def ChooseAIMove():
    # 1) Win if possible
    move = find_winning_move("O")
    if move:
        return move

    # 2) Block opponent win
    move = find_winning_move("X")
    if move:
        return move

    # 3) Take center if available (for odd board)
    if AmountOfSquare % 2 == 1:
        center = ((AmountOfSquare - 1) // 2, (AmountOfSquare - 1) // 2)
        if get_owner(*center) is None:
            return center

    # 4) Take a corner if available
    corners = [(0, 0), (AmountOfSquare - 1, 0), (0, AmountOfSquare - 1), (AmountOfSquare - 1, AmountOfSquare - 1)]
    available_corners = [c for c in corners if get_owner(*c) is None]
    if available_corners:
        return random.choice(available_corners)

    # 5) Otherwise pick any random empty cell
    empties = []
    for x in range(AmountOfSquare):
        for y in range(AmountOfSquare):
            if get_owner(x, y) is None:
                empties.append((x, y))
    if empties:
        return random.choice(empties)

    return None

#I have read through the AI generated code, and I do understand what it all means and how to replicate it if needed.

def Loop():
    global Drawing
    global CurrentTileX
    global CurrentTileY
    global OccupiedSpots
    global Won
    global SB
    if Drawing == False:
        CO.setpos(-100-(50*(AmountOfSquare-3))+(100*CurrentTileX),-100-(50*(AmountOfSquare-3))+(100*CurrentTileY))

    if Player == 1:
        CO.shape('square')
    if Player == 2:
        CO.shape('circle')

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
    if Winner != None and Won == False:
        Won = True
        Drawing = False
        Score[Winner] += 1
        DrawTextScore()
        DrawTextWinner(Winner)
    
    '''if PlayerMode == "Computer" and Player == 2:
        Xchosen = random.randint(0, AmountOfSquare-1)
        Ychosen = random.randint(0, AmountOfSquare-1)
        #print(OccupiedSpots)
        check = False
        for i in OccupiedSpots:
            if f"({Xchosen}, {Ychosen})" == str(i["Pos"]):
                check = True

        if check == False:
            DrawCircleManual((Xchosen, Ychosen))'''
    
    if PlayerMode == "Computer" and Player == 2:
        # smarter AI:
        if ComputerMode == "Random":
            Xchosen = random.randint(0, AmountOfSquare-1)
            Ychosen = random.randint(0, AmountOfSquare-1)
            #print(OccupiedSpots)
            check = False
            for i in OccupiedSpots:
                if f"({Xchosen}, {Ychosen})" == str(i["Pos"]):
                    check = True

            if check == False:
                DrawCircleManual((Xchosen, Ychosen))
        elif ComputerMode == "Smart":
            move = ChooseAIMove()
            if move is not None:
                # move is (x_index, y_index)
                DrawCircleManual(move)



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
        elif PlayerMode == "Player":
            DrawCircle((-100-(50*(AmountOfSquare-3))+(100*CurrentTileX),-100-(50*(AmountOfSquare-3))+(100*CurrentTileY)))

def ResetBoard():
    print("")
    global GS
    global CO
    global SB
    global Won
    global OccupiedSpots
    global Player
    OccupiedSpots = []
    Player = 1
    GS.clear()
    CO.clear()
    SB.clear()
    DrawTextScore()
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