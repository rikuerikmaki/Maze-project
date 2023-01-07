import queue
import maze

def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == True:
            start_x = x
            start_y = 0

    i = start_x
    j = start_y
    for move in moves:
        if move == "W":
            i -= 1

        elif move == "E":
            i += 1

        elif move == "N":
            j -= 1

        elif move == "S":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze.checkCell(j, i) == False):
            return False

    return True


def findEnd(maze, moves):
    
    for r in range(len(maze) - 1):
        for x, pos in enumerate(maze[r]):
            if pos == True:
                start_x = x
                start_y = r

    i = start_x
    j = start_y
    for move in moves:
        if move == "W":
            i -= 1

        elif move == "E":
            i += 1

        elif move == "N":
            j -= 1

        elif move == "S":
            j += 1

    if maze[j][i] == "M":
        print("Found: " + moves)
        return True

    return False

nums = queue.Queue()
nums.put("")
add = ""
maze = maze.Maze(40, 40, 1000, 1000)

while not findEnd(maze, add): 
    add = nums.get()
    #print(add)
    for j in ["W", "E", "N", "S"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)