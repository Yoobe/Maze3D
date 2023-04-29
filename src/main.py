from data import *
from hp48fonts import *

from hpprime import *


# Keyboard
def GetKey():  # determine  what to do next
    keyCode = 0
    if keyboard():
        keyCode = eval('GETKEY()')
    return keyCode

# Main function
def main():
    global pX, pY, pO
    # init Screen
    resetScreen()
    # textout(0, 225, 5, "Loading...", black)
    
    drawEmptyMaze()
    # textout(0, 225, 15, "Maze Map", black)
    
    LoadScreens()
    # textout(0, 225, 25, "Load Screens", black)
    
    Dashboard()
    
    # load maze screen 1 as starting point
    # textout(0, 225, 35, "First screen", black)
    ShowScreen(GetScreenId(pX, pY, pO))
    # Show Arrow at start position
    ShowArrow(pX, pY, pO)
    # ShowArrow(1, 1, 1)
    # ShowArrow(2, 2, 2)
    # ShowArrow(3, 3, 4)
    Disclose(pX, pY)
    
    # open all
    # for x in range (X):
    #     for y in range (Y):
    #         Disclose(x, y)
    
    textout48(300, 230, "Maze 3D", 0x121212, 's')
    # textout48(228, 16, "Commands:", 0x121212, 's')
    # textout48(228, 23, "UP: Move Forward", 0x121212, 's')
    # textout48(228, 30, "LEFT: Rotate left", 0x121212, 's')
    # textout48(228, 37, "RIGHT: Rotate Right", 0x121212, 's')
    # textout48(228, 44, "ON: Exit", 0x121212, 's')
    
    # textout(0, 225, 45, "Arrows to move", black)
    
    complete = False
    
    while True:        
        k = GetKey()
        
        if k > 0:
            if k == 46:   # Press ON to leave game
                break
            
            if k == 2 and complete == False: # UP
                if GoForward():
                    complete = True
            if k == 7 and complete == False: # LEFT
                TurnLeft()    
            if k == 8 and complete == False: # RIGHT
                TurnRight()            

# Start Main loop
main()