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
    '''
    Generate a maze and return its walls
    Return type (x_walls, y_walls)
    x_walls/y_walls - bool array, True = wall, False = no wall
    x_walls/y_walls ordered from left to right / top to bottom
    '''
    global maze
    visited = [[False for x in range(X)] for y in range(Y)]
    # x_walls = [[1 for x in range(X)] for y in range(Y+1)]
    # y_walls = [[1 for x in range(X+1)] for y in range(Y)]
    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # for dby in range(Y):
        # print(maze[dby])

    stack = [(randint(0, 19), randint(0, 7), 0, 0)]
    while stack:
        xo, yo, x, y = stack.pop()
        # print("While on", xo, yo, x, y)
        if visited[y][x]:
            continue
        visited[y][x] = True
        # print("1 - cell", x, y,f'{maze[y][x]:04b}')
        # print("3 - cell", xo, yo, f'{maze[yo][xo]:04b}')
        
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
        
        # print("2 - cell", x, y, f'{maze[y][x]:04b}')
        # print("3 - cell", xo, yo, f'{maze[yo][xo]:04b}')

        # for dby in range(Y):
            # print(maze[dby])

        random_shuffle(moves)
        # print("moves", moves)
        for dx, dy in moves:
            # print("Move", dx, dy, x, y)
            xn = x+dx
            yn = y+dy
            # print("Move", xn, yn, x, y)
            if xn < 0 or xn >= X or yn < 0 or yn >= Y:
                # print("Ignored", xn, yn)
                continue
            stack += [(x, y, xn, yn)]
            # print("staked", stack)
    return maze

if __name__ == '__main__':
    maze = generate_maze()
    for dby in range(Y):
        print(maze[dby])
    # for y in range(Y):
        # print(" ", x_walls[y])
        # print(y_walls[y])
    # print(" ", x_walls[8])