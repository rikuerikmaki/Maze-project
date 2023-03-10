import queue
import numpy as np
import random


#ALGORITHM THAT SOLVES THE PATH WITH DEPTH-FIRST-SEARCH.


def get_neighbors(i, j, rows, columns):

    arr = []
    if i != 0:
        arr.append([i - 1, j])
    if i < rows:
        arr.append([i + 1, j])
    if j != 0:
        arr.append([i, j - 1])
    if j < columns:
        arr.append([i, j + 1])
    random.shuffle(arr)
    return arr


def findPath(maze, start):
    q = []
    q.append(start)
    rows = maze.get_rows()
    columns = maze.get_columns()
    visited = []
    for i in range(rows):
        hold = []
        for j in range(columns):
            hold.append(False)
        visited.append(hold)

    visited[start[0]][start[1]] = True
    prev = []
    for i in range(rows):
        hold = []
        for j in range(columns):
            hold.append([i, j])
        prev.append(hold)


    while not len(q) == 0:
        node = q.pop()
        neighours = get_neighbors(node[0], node[1], rows, columns)
        direction = ""
        for next in neighours:
            if node[0] - next[0] == -1:
                direction = "Left"
            if node[0] - next[0] == 1:
                direction = "Right"
            if node[1] - next[1] == -1:
                direction = "Up"
            if node[1] - next[1] == 1:
                direction = "Down"
            if not maze.hasWall2(next[1], next[0], direction):
                if not visited[next[0]][next[1]]:
                    visited[next[0]][next[1]] = True
                    q.append(next)
                    prev[next[0]][next[1]] = node
    return prev


def create_path(start, end, maze):
    parents = findPath(maze, start)
    path = []
    node = end
    while node != start:
        path.append(node)
        print(node)
        node = parents[node[0]][node[1]]
    path.append([0,0])
    print(path)
    return path
        
