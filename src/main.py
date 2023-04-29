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
    
    drawEmptyMaze()
    
    LoadScreens()
    
    Dashboard()
    
    # load maze screen 1 as starting point
    ShowScreen(GetScreenId(pX, pY, pO))

    # Show Arrow at start position
    ShowArrow(pX, pY, pO)

    Disclose(pX, pY)
    
    textout48(300, 230, "Maze 3D", 0x121212, 's')
    
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