import random as rnd

from copy import deepcopy


def printBoard(board):
    for row in board:
        print(row)
    return


def isAlive(board, row, column):
    return board[row][column] == 1


def killCell(board, row, column):
    board[row][column] = 0
    return


def newCell(board, row, column):
    board[row][column] = 1
    return


def getAliveNeighboursCount(board, row, column):
    size = len(board)

    rows = list({max(0, row - 1), row, min(size - 1, row + 1)})
    columns = list({max(0, column - 1), column, min(size - 1, column + 1)})

    total = 0
    for i in rows:
        for j in columns:
            total += board[i][j]

    return total - board[row][column]


size = 10
minAllowedNeighbours = 2
maxAllowedNeighbours = 3
maxParentCount = 3

universe = [[rnd.randint(0, 1) for x in range(size)] for y in range(size)]

printBoard(universe)
print()

for epoch in range(10):
    buffer = deepcopy(universe)
    for row in range(size):
        for column in range(size):
            neighbours = getAliveNeighboursCount(universe, row, column)

            if isAlive(universe, row, column):
                if neighbours > maxAllowedNeighbours or neighbours < minAllowedNeighbours:
                    killCell(buffer, row, column)
            else:
                if neighbours == maxParentCount:
                    newCell(buffer, row, column)
    universe = buffer

    print("Epoch : {}\n".format(epoch))
    printBoard(universe)
    print("\n\n")
