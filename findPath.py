import queue


def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "#","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", "E", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "M","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "E", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "M", "#"])

    return maze

def createMaze3():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#", "E", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])



def printMaze(maze, path=""):

    for r in range(len(maze) - 1):
        for x, pos in enumerate(maze[r]):
            if pos == "E":
                start_x = x
                start_y = r

    i = start_x
    j = start_y
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for r in range(len(maze) - 1):
        for x, pos in enumerate(maze[r]):
            if pos == "E":
                start_x = x
                start_y = r

    i = start_x
    j = start_y
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    
    for r in range(len(maze) - 1):
        for x, pos in enumerate(maze[r]):
            if pos == "E":
                start_x = x
                start_y = r

    i = start_x
    j = start_y
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "M":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False

nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze()

while not findEnd(maze, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)