from hpprime import *
from maze import *
from hp48fonts import *

# Maze data

# Maze definition (NESW) 
# MazeBox = [0b0000, 0b0100, 0b0010, 0b0001, 0b1000, 0b0101, 0b1010, 0b0111, 0b1011, 0b1101, 0b1110, 0b0011, 0b1001, 0b1100, 0b0110, 0b1111, 999]
MazeBox = [0b0000, 0b0001, 0b0010, 0b0011, 0b0100, 0b0101, 0b0110, 0b0111, 0b1000, 0b1001, 0b1010, 0b1011, 0b1100, 0b1101, 0b1110, 0b1111]
# Maze = [[1,5,11,14,5,11,14,5,5,5,5,5,11,1,5,7,11,2,14,11],[14,3,6,13,11,6,13,5,5,5,11,2,6,14,3,6,6,6,6,6],[6,1,9,5,8,13,5,5,5,3,6,6,6,6,14,12,13,9,12,6],[6,14,11,2,6,14,5,7,5,5,12,6,6,6,10,5,3,1,5,8],[6,6,13,8,6,10,11,13,5,3,14,15,12,10,9,5,5,11,14,8],[10,12,14,8,6,4,6,14,5,11,4,6,14,9,5,5,11,6,6,4],[10,5,12,6,13,5,12,10,3,13,5,12,4,14,7,11,4,6,10,11],[4,1,5,9,5,5,5,9,5,5,5,5,5,12,4,13,5,12,4,16]]
Maze = generate_maze()
Img = ["img1.png", "img2.png", "img3.png", "img4.png", "img5.png", "img6.png", "img7.png", "img8.png", "img9.png"]
ImgType = [0b010, 0b000, 0b100, 0b001, 0b101, 0b111, 0b011, 0b110] 
Arrow = [[0, 0, 1, 1, 0, 0, 0], [0, 0, 0 ,1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0 ,1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0]]

# Color codes
black = 0x000000
white = 0xf8f8f8
blue = 0x0000f8
green = 0x00f800
red = 0xf80000
cyan = 0x00f8f8
magenta = 0xf800f8
yellow = 0xf8f800
cArrow = 0x2072cb

# Definition of Orientation
# 1 = North
NORTH = 1
# 2 = East
EAST = 2
# 3 = South
SOUTH = 3
# 4 = West
WEST = 4

# Player data
pO = 2 # starting orientation is East  
pX = 0 # starting X  
pY = 0 # starting Y 
pF = 1 # boolean to check if FW it open
pView = MazeBox[Maze[pY][pX]]
pScore = 0

# Reset Screen Function
def resetScreen():
    fillrect(0, 0, 0, 320, 240, white, white)
    # eval("G0:=AFiles(\"bg.png\")")
    # fillrect(0, 0, 121, 241, 176-121, bg, bg)
    # fillrect(0, 0, 194, 320, 240, white, white)
    # eval("G0:=AFiles(\"" + Img[0] + "\")")

def drawEmptyMaze():
    # 7 , 156 -> 216, 235
    for x in range (21):
        line(0, 7 + x * 10, 156, 7 + x * 10, 236, black)
    for y in range (9):
        line(0, 7, 156 + y * 10 , 207, 156 + y * 10, black)

def LoadScreens():
    eval("G1:=AFiles(\"" + Img[0] + "\")")
    eval("G2:=AFiles(\"" + Img[1] + "\")")
    eval("G3:=AFiles(\"" + Img[2] + "\")")
    eval("G4:=AFiles(\"" + Img[3] + "\")")
    eval("G5:=AFiles(\"" + Img[4] + "\")")
    eval("G6:=AFiles(\"" + Img[5] + "\")")
    eval("G7:=AFiles(\"" + Img[6] + "\")")
    eval("G8:=AFiles(\"" + Img[7] + "\")")
    eval("G9:=AFiles(\"" + Img[8] + "\")") # 219-86 -> 318-190

def Dashboard(): 
    strblit2(0, 219, 0, 100, 78, 9, 219, 0, 100, 78)
    
    # strblit2(0, 219, 86, 99, 104, 9, 219, 86, 99, 104)

def ShowScreen(index):
    strblit2(0, 7, 2, 209, 149, index, 7, 2, 209, 149)
    
def ShowArrow(x, y, o):
    if o == NORTH:
        for i in range(7):
            for j in range(7):
                if Arrow[i][j] == 1:
                    pixon(0, x * 10 + 9 + i, y  * 10 + 158 + 6 - j, cArrow)
    if o == SOUTH:
        for i in range(7):
            for j in range(7):
                if Arrow[6-i][j] == 1:
                    pixon(0, x * 10 + 9 + i, y  * 10 + 158 + j, cArrow)
    if o == EAST:
        for i in range(7):
            for j in range(7):
                if Arrow[j][i] == 1:
                    pixon(0, x * 10 + 9 + i, y  * 10 + 158 + j, cArrow)
    if o == WEST:
        for i in range(7):
            for j in range(7):
                if Arrow[j][i] == 1:
                    pixon(0, x * 10 + 9 + 6 - i, y  * 10 + 158 + j, cArrow)

def CleanArrow(x, y):
    fillrect(0, x * 10 + 9, y * 10 + 158, 7, 7, white, white)

def DropPoint(x, y):
    fillrect(0, x * 10 + 11, y * 10 + 160, 3, 3, red, red)

def Disclose(x, y):
    # if Maze[y][x] == 0:
        # old close
    if Maze[y][x] == 4:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
    elif Maze[y][x] == 2:
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white) # S
    elif Maze[y][x] == 1:
        line(0, 7 + x * 10, 156 + y * 10 + 1, 7 + x * 10, 156 + y * 10 + 9, white) # W
    elif Maze[y][x] == 8:
        line(0, 7 + x * 10 + 1, 156 + y * 10, 7 + x * 10 + 9, 156 + y * 10, white) # N
    elif Maze[y][x] == 5:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
        line(0, 7 + x * 10, 156 + y * 10 + 1, 7 + x * 10, 156 + y * 10 + 9, white)
    elif Maze[y][x] == 10:
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white)            
        line(0, 7 + x * 10 + 1, 156 + y * 10, 7 + x * 10 + 9, 156 + y * 10, white)    
    elif Maze[y][x] == 7:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white)
        line(0, 7 + x * 10, 156 + y * 10 + 1, 7 + x * 10, 156 + y * 10 + 9, white)
    elif Maze[y][x] == 11:
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white)
        line(0, 7 + x * 10, 156 + y * 10 + 1, 7 + x * 10, 156 + y * 10 + 9, white)
        line(0, 7 + x * 10 + 1, 156 + y * 10, 7 + x * 10 + 9, 156 + y * 10, white)  
    elif Maze[y][x] == 13:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
        line(0, 7 + x * 10, 156 + y * 10 + 1, 7 + x * 10, 156 + y * 10 + 9, white)
        line(0, 7 + x * 10 + 1, 156 + y * 10, 7 + x * 10 + 9, 156 + y * 10, white)  
    elif Maze[y][x] == 14:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white) # S
        line(0, 7 + x * 10 + 1, 156 + y * 10, 7 + x * 10 + 9, 156 + y * 10, white) # N 
    elif Maze[y][x] == 3:
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white)
        line(0, 7 + x * 10, 156 + y * 10 + 1, 7 + x * 10, 156 + y * 10 + 9, white)
    elif Maze[y][x] == 9:
        line(0, 7 + x * 10, 156 + y * 10 + 1, 7 + x * 10, 156 + y * 10 + 9, white)
        line(0, 7 + x * 10 + 1, 156 + y * 10, 7 + x * 10 + 9, 156 + y * 10, white)  
    elif Maze[y][x] == 12:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
        line(0, 7 + x * 10 + 1, 156 + y * 10, 7 + x * 10 + 9, 156 + y * 10, white)  
    elif Maze[y][x] == 6:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white) # S
    elif Maze[y][x] == 15:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white)
        line(0, 7 + x * 10, 156 + y * 10 + 1, 7 + x * 10, 156 + y * 10 + 9, white)
        line(0, 7 + x * 10 + 1, 156 + y * 10, 7 + x * 10 + 9, 156 + y * 10, white)  
    elif Maze[y][x] == 16:
        line(0, 7 + x * 10 + 10, 156 + y * 10 + 1, 7 + x * 10 + 10, 156 + y * 10 + 9, white) # E
        line(0, 7 + x * 10 + 1, 156 + y * 10 + 10, 7 + x * 10 + 9, 156 + y * 10 + 10, white) # S

def GetScreenId(x, y, o):
    global NORTH, SOUTH, EAST, WEST
    BoxInfo = MazeBox[Maze[y][x]]
    Value = -1
    if o == NORTH: # North
        # North bit -> Front (Middle)
        # East bit -> Right
        # West bit -> Left
        Value = ((BoxInfo & 0b1000) >> 2) | ((BoxInfo & 0b0100) >> 2) | ((BoxInfo & 0b0001) << 2)
    elif o == SOUTH: # South
        # South bit -> Front (Middle)
        # West bit -> Right
        # East bit -> Left
        # Value = BoxInfo & 0b0010 | BoxInfo & 0b0001 | BoxInfo & 0b0100 
        Value = BoxInfo & 0b0111
    elif o == EAST: # East
        # East bit -> Front (Middle)
        # West bit -> Right
        # North bit -> Left
        # Value = BoxInfo & 0b1000 >> 1 | BoxInfo & 0b0010 >> 1 | BoxInfo & 0b0100 >> 1
        Value = (BoxInfo & 0b1110) >> 1
    elif o == WEST: # West
        # West bit -> Front (Middle)
        # North bit -> Right
        # South bit -> Left
        Value = ((BoxInfo & 0b0001) << 1) | ((BoxInfo & 0b1000) >> 3) | ((BoxInfo & 0b0010) << 1)
        
    for i in range(len(ImgType)):
        if ImgType[i] == Value:
            return i
    
    return -1

def GoForward():
    global pX, pY, pO, pF, pView, pScore
    x = pX
    y = pY
    pF = 0 # reset FW is open bool
    # check if FW is open
    if pO == NORTH: # North
        if (pView & 0b1000) == 0b1000: # North is open
            pF = 1
            y = pY - 1
    elif pO == SOUTH: # South
        if (pView & 0b0010) == 0b0010: # South is open
            pF = 1
            y = pY + 1
    elif pO == EAST: # East
        if (pView & 0b0100) == 0b0100: # East is open
            pF = 1
            x = pX + 1
    elif pO == WEST: # West
        if (pView & 0b0001) == 0b0001: # West is open
            pF = 1
            x = pX - 1
    
    if pF == 1: # If FW is open, go to next position
        # Clean current Arrow
        CleanArrow(pX, pY)
        DropPoint(pX, pY)
        
        # Disclose the cell in previous position
        Disclose(pX, pY)
        
        # Set new Coordinate
        pX = x
        pY = y
        
        # Draw new Arrow
        ShowArrow(pX, pY, pO)
        
        # Update Score
        pScore += 1
        Score()
        
        # Compute new Screen
        index = GetScreenId(pX, pY, pO)
        pView = MazeBox[Maze[y][x]]
        
        # Update the Screen
        ShowScreen(index+1)
        
        # Check if game completed successfully
        if x == 19 and y == 7: # Last cell bottom right
            ShowWinMsg()
            return 1
    return 0

# Player rotate to left
def TurnLeft(): 
    global pO, pX, pY
    pO -= 1
    if pO == 0:
        pO = 4
    
    #refresh
    CleanArrow(pX, pY)

    # Draw new Arrow
    ShowArrow(pX, pY, pO)

    # Compute new Screen
    index = GetScreenId(pX, pY, pO)

    # Update the Screen
    ShowScreen(index+1)

# Player rotate to left
def TurnRight(): 
    global pO, pX, pY
    pO += 1
    if pO == 5:
        pO = 1
        #refresh
    CleanArrow(pX, pY)

    # Draw new Arrow
    ShowArrow(pX, pY, pO)

    # Compute new Screen
    index = GetScreenId(pX, pY, pO)

    # Update the Screen
    ShowScreen(index+1)
    
def Score():
    global pScore
    fillrect(0, 264, 13, 11, 5, white, white)
    textout48(264, 13, str(pScore), 0x121212, 's')
    
def ShowWinMsg(): # 219-86 -> 318-190
    strblit2(0, 219, 86, 99, 104, 9, 219, 86, 99, 104)