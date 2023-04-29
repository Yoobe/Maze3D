try:
    from urandom import *
    platform = "hp"
except ImportError or ModuleNotFoundError:
    from random import *
    platform = "win"
    
X = 20
Y = 8
maze = [[0 for _ in range(X)] for _ in range(Y)]

def UpdateMaze(x, y, value):
    global X, Y, maze
    if x < 0 or x >= X or y < 0 or y >= Y:
        return
    else:
        maze[y][x] |= value

def random_shuffle(seq):
    l = len(seq)
    for i in range(l):
        j = randrange(l)
        seq[i], seq[j] = seq[j], seq[i]

def generate_maze():
    global maze
    visited = [[False for x in range(X)] for y in range(Y)]
    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    stack = [(randint(0, 19), randint(0, 7), 0, 0)]
    while stack:
        xo, yo, x, y = stack.pop()
        if visited[y][x]:
            continue
        visited[y][x] = True
        
        if x > xo: # we moved right
            UpdateMaze(xo, yo, 0b0100)
            UpdateMaze(x, y, 0b0001)
            # print("R")
        if x < xo: # we moved left
            UpdateMaze(xo, yo, 0b0001)
            UpdateMaze(x, y, 0b0100)
            # print("L")
        if y > yo: # we moved down
            UpdateMaze(xo, yo, 0b0010)
            UpdateMaze(x, y, 0b1000)
            # print("D")
        if y < yo: # we moved up
            UpdateMaze(xo, yo, 0b1000)
            UpdateMaze(x, y, 0b0010)
            # print("U")

        random_shuffle(moves)
        for dx, dy in moves:
            xn = x+dx
            yn = y+dy
            if xn < 0 or xn >= X or yn < 0 or yn >= Y:
                continue
            stack += [(x, y, xn, yn)]
    return maze
