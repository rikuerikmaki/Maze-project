import random
import numpy as np
import math
import findPath as fp
from tkinter import Tk, Canvas


class Maze:
    def __init__(self, rows, columns, width, height):
        self.root = Tk()
        self.root.title("Mouse in a Maze")
        self.canvas = Canvas(self.root, bg="#7e95be", width=1080, height=1080)
        self.canvas.pack()
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.horizontalWalls = np.full((rows + 1, columns), True)
        self.verticalWalls = np.full((rows, columns + 1), True)
        #self.horizontalWalls[0][0] = False
        #self.horizontalWalls[rows][columns - 1] = False
        self.maze = self.generate(None)
        self.edge = self.width / 5
        self.mice = []
        self.thickness = 1
        self.cell_w = math.floor((self.width - self.edge) / len(self.horizontalWalls[0]))
        self.cell_h = math.floor((self.height - self.edge) / len(self.verticalWalls))
        self.start = [0,0]
        self.end = [self.rows - 1, self.columns - 1]

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def hasVerticalWall(self, row, column):
        return self.verticalWalls[row][column]

    def hasHorizontalWall(self, row, column):
        return self.horizontalWalls[row][column]

    def hasWall(self, row, column, direction):
        if direction == "Up":
            return self.horizontalWalls[row+1][column]
        if direction == "Down":
            return self.horizontalWalls[row][column]
        if direction == "Left":
            return self.verticalWalls[row][column]
        if direction == "Right":
            return self.verticalWalls[row][column + 1]

    def hasWall2(self, row, column, direction):
        if direction == "Up":
            return self.horizontalWalls[row][column]
        if direction == "Down":
            return self.horizontalWalls[row + 1][column]
        if direction == "Left":
            return self.verticalWalls[row][column]
        if direction == "Right":
            return self.verticalWalls[row][column + 1]

    def breakWall(self, row, column, direction):
        if (0 <= row and row < self.rows) and (0 <= column and column < self.columns):
            if direction == "Up" and (row != self.rows+1):
                self.horizontalWalls[row + 1][column] = False
            if direction == "Down" and (row != 0):
                self.horizontalWalls[row][column] = False
            if direction == "Left" and (column != 0):
                self.verticalWalls[row][column] = False
            if direction == "Right" and (column != self.columns -1):
                self.verticalWalls[row][column + 1] = False

    def checkReachability(self):
        seen = np.full((self.rows, self.columns), False)
        queue = []
        queue.append([0,0])
        seen[0][0] = True
        while queue:
            [r, c] = queue.pop(0)
            if r > 0 and not seen[r-1][c] and not self.hasWall(r,c,"Down"):
                queue.append([r-1,c])
                seen[r-1][c] = True
            if r < self.rows -1 and not seen[r+1][c] and not self.hasWall(r,c,"Up"):
                queue.append([r+1,c])
                seen[r+1][c] = True
            if c > 0 and not seen[r][c-1] and not self.hasWall(r,c,"Left"):
                queue.append([r,c-1])
                seen[r][c-1] = True
            if c < self.columns -1 and not seen[r][c+1] and not self.hasWall(r,c,"Right"):
                queue.append([r,c+1])
                seen[r][c+1] = True
        for i in range(len(seen)):
            for p in range(len(seen[i])):
                if not seen[i][p]:
                    return False
        return True


    def show(self):
        matrix = ""
        horizontal_string = "".join("-" if b else ' ' for i, b in enumerate(self.horizontalWalls[0]))
        horizontal_string = "+".join(horizontal_string[i:i + 1] for i in range(0, len(horizontal_string), 1))
        matrix += "*" + horizontal_string + "*"  + "\n"
        for p in range(1,self.rows):
            vertical_string = "".join("|" if b else ' ' for i, b in enumerate(self.verticalWalls[p]))
            vertical_string = " ".join(vertical_string[i:i + 1] for i in range(0, len(vertical_string), 1))+"\n"
            matrix += vertical_string
            horizontal_string = "".join("-" if b else ' ' for i, b in enumerate(self.horizontalWalls[p]))
            horizontal_string = "+".join(horizontal_string[i:i + 1] for i in range(0, len(horizontal_string), 1))
            matrix += "*" + horizontal_string + "*" + "\n"
        return matrix

    def draw(self):
        edge = self.edge / 2
        for y in range(len(self.verticalWalls)):
            for x, isWall in enumerate(self.verticalWalls[y]):
                if isWall:
                    self.canvas.create_line(x*self.cell_w + edge, y*self.cell_h + edge, x*self.cell_w + edge, y*self.cell_h + self.cell_h + (self.thickness -1) + edge, width=self.thickness, fill = "#4D3F3C", tag="line")
        for y in range(len(self.horizontalWalls)):
            for x, isWall in enumerate(self.horizontalWalls[y]):
                if isWall:
                    self.canvas.create_line(x*self.cell_w + edge, y*self.cell_h + edge, x*self.cell_w + self.cell_w + (self.thickness -1) + edge, y*self.cell_h + edge, width=self.thickness, fill = "#4D3F3C", tag="line")


    def generate(self, seed):
        rand = random.seed(seed)
        seen = np.full((self.rows, self.columns), False)

        queue = []
        queue2 = []

        queue.append([0,0])
        queue2.append([0, 0])
        seen[0][0] = True

        while bool(queue):
            [row, column] = queue.pop(0)
            neighbours = self.getNeighbours(row, column)
            index = 0
            while index < len(neighbours):
                neigh = neighbours[index]

                if not seen[neigh[0]][neigh[1]]:
                    seen[neigh[0]][neigh[1]] = True
                    queue.append(neigh)
                    queue2.append(neigh)
                    dx = neigh[1] - column
                    if dx == 1 and self.hasWall(row, column, "Right"):
                        self.breakWall(row, column, "Right")
                    elif dx == -1 and self.hasWall(row, column, "Left"):
                        self.breakWall(row, column, "Left")
                    dy = neigh[0]-row
                    if dy == 1 and self.hasWall(row, column, "Up"):
                        self.breakWall(row, column, "Up")
                    if dy == -1 and self.hasWall(row, column, "Down"):
                        self.breakWall(row, column, "Down")
                    index = len(neighbours)
                index += 1
            if index == len(neighbours) and len(queue2) > 0:
                queue.append(queue2.pop(0))

    def getNeighbours(self, row, column):
        neighbours = []
        top = [row, column - 1]
        bottom = [row, column + 1]
        left = [row - 1, column]
        right = [row + 1, column]

        if self.checkCell(top[0], top[1]):
            neighbours.append(top)
        if self.checkCell(bottom[0], bottom[1]):
            neighbours.append(bottom)
        if self.checkCell(left[0], left[1]):
            neighbours.append(left)
        if self.checkCell(right[0], right[1]):
            neighbours.append(right)

        random.shuffle(neighbours)
        return neighbours


    def checkCell(self, row, column):
        if row < 0 or row > self.rows -1 or column < 0 or column  > self.columns -1:
            return False
        return True

    def create_mouse(self, position, start, number):
        for i in range(number):
            self.mice.append([position, start, 0])

    def draw_mice(self, color):
        for mouse in self.mice:
            x1, y1 = (mouse[0][0] * self.cell_w + self.edge/2 + mouse[1][0], mouse[0][1] * self.cell_h + self.edge/2 + mouse[1][1])
            x2, y2 = (x1 + self.cell_w / 10, y1 + self.cell_h / 10)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def move_mice(self):
        finnish = False
        self.draw_mice("#7e95be")
        for index, mouse in enumerate(self.mice):
            moves = ["N", "E", "S", "W"]
            move = random.choice(moves)
            print(mouse)
            pos_y = mouse[0][0]
            pos_x = mouse[0][1]
            #print(self.hasWall2(pos_x, pos_y, "Up"), "Up")
            #print(self.hasWall2(pos_x, pos_y, "Left"), "Left")
            #print(self.hasWall2(pos_x, pos_y, "Down"), "Down")
            #print(self.hasWall2(pos_x, pos_y, "Right"), "Right")

            if move == "N" and mouse[1][1] != 0:
                if not self.hasWall2(pos_x, pos_y, "Up") or mouse[1][1] != 1:
                    self.mice[index][1][1] -= 1

            elif move == "N" and mouse[1][1] == 0 and not self.hasWall2(pos_x, pos_y, "Up"):
                self.mice[index][0][1] -= 1
                self.mice[index][1][1] = self.cell_h - 1

            if move == "E" and mouse[1][0] != self.cell_w -1:
                if not self.hasWall2(pos_x, pos_y, "Right") or mouse[1][0] != self.cell_w - 2:
                    self.mice[index][1][0] += 1

            elif move == "E" and mouse[1][0] == self.cell_w -1 and not self.hasWall2(pos_x, pos_y, "Right"):
                self.mice[index][0][0] += 1
                self.mice[index][1][0] = 0

            if move == "S" and mouse[1][1] != self.cell_h -1:
                if not self.hasWall2(pos_x, pos_y, "Down") or mouse[1][1] != self.cell_h - 2:
                    self.mice[index][1][1] += 1

            elif move == "S" and mouse[1][1] == self.cell_h -1 and not self.hasWall2(pos_x, pos_y, "Down"):
                print("hellosss")
                self.mice[index][0][1] += 1
                self.mice[index][1][1] = 0

            if move == "W" and mouse[1][0] != 0:
                if not self.hasWall2(pos_x, pos_y, "Left") or mouse[1][0] != 1:
                    self.mice[index][1][0] -= 1

            elif move == "W" and mouse[1][0] == 0 and not self.hasWall2(pos_x, pos_y, "Left"):
                self.mice[index][0][0] -= 1
                self.mice[index][1][0] = self.cell_w - 1
        self.draw_mice("green")
        if finnish == False:
            self.root.after(10, self.move_mice)



    def draw_path(self, path, color):
        for step in path:
            x1, y1 = (step[0] * self.cell_w + self.edge / 2 + self.cell_w / 3, step[1] * self.cell_h + self.edge / 2 + self.cell_h / 3)
            x2, y2 = (x1 + self.cell_w / 3, y1 + self.cell_h / 3)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")


    def draw_path(self, path, color):
        for step in path:
            x1, y1 = (step[0] * self.cell_w + self.edge / 2 + self.cell_w / 3, step[1] * self.cell_h + self.edge / 2 + self.cell_h / 3)
            x2, y2 = (x1 + self.cell_w / 3, y1 + self.cell_h / 3)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")



    def main(self):
        maze.draw()
        maze.create_mouse(self.start, [5, 5], 1)
        print(self.horizontalWalls)
        print(self.verticalWalls)
        print(self.hasWall(0, 0, "Up"))
        print(self.hasWall(0, 0, "Left"))
        print(self.hasWall(0, 0, "Down"))
        print(self.hasWall(0, 0, "Right"))
        maze.draw_mice("green")
        result = fp.create_path(self.start, self.end, maze)
        self.draw_path(result, "Blue")
        print(len(result))
        #maze.move_mice()
        #print(maze.show())
        self.root.mainloop()

maze = Maze(6, 10, 1000, 1000)
maze.main()


