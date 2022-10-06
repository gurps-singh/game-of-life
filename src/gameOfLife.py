import random

import numpy as np


def initialiseGrid(rows, columns):
    return [[0 for x in range(columns)] for y in range(rows)]


def randomiseGrid(rows, columns):
    initialGrid = initialiseGrid(rows, columns)
    for i in range(rows):
        for j in range(columns):
            randomValue = random.randint(0, 1)
            initialGrid[i][j] = randomValue
    return initialGrid


def getNumberOfRowsInGrid(grid):
    return len(grid)


def getNumberOfColumnsInGrid(grid):
    return len(grid[0])


def nextGenerationGrid(grid):
    numberOfRowsInGrid = getNumberOfRowsInGrid(grid)
    numberOfColumnsInGrid = getNumberOfColumnsInGrid(grid)
    nextGenerationState = initialiseGrid(numberOfRowsInGrid, numberOfColumnsInGrid)

    for i in range(0, numberOfRowsInGrid):
        for j in range(0, numberOfColumnsInGrid):
            nextGenerationState[i][j] = nextGenerationValue(i, j, numberOfRowsInGrid, numberOfColumnsInGrid, grid)

    return nextGenerationState


def nextGenerationValue(currentRow, currentColumn, numberOfRowsInGrid, numberOfColumnsInGrid, grid):
    originalLiveNeighbour = 0
    for i in range(currentRow - 1, currentRow + 2):
        for j in range(currentColumn - 1, currentColumn + 2):
            # check row wise going off grid, column wise going off grid and not to count the current position as it is the original position we started at
            if i < 0 or i >= numberOfRowsInGrid or j < 0 or j >= numberOfColumnsInGrid or (
                    i == currentRow and j == currentColumn):
                continue
            if grid[i][j] == 1:
                originalLiveNeighbour += 1

    # if the cell is alive
    if grid[currentRow][currentColumn] == 1:

        # Any live cell with fewer than two live neighbours dies, as if caused by underpopulation
        if originalLiveNeighbour <= 1:
            return 0

        # Any live cell with two or three live neighbours lives on to the next generation
        elif originalLiveNeighbour in (2, 3):
            return 1

        # Any live cell with moree than three live neighbours dies, as if caused by overcrowding
        else:
            return 0

    # if the cell is dead
    else:
        # Any dead cell with exactly three live neighbours becomes a live cell
        if originalLiveNeighbour == 3:
            return 1
        else:
            return 0


def runGameOfLife(numberOfRows, numberOfColumns, option):
    if numberOfColumns > 100 or numberOfRows > 100:
        print('The number of rows or columns specified is above the limit permitted, please use a lower value')
        exit(1)
    counter = 0
    if option == 1:
        grid = randomiseGrid(numberOfRows, numberOfColumns)
        print('Generation ', counter)
        print(np.matrix(grid))
        numberOfGenerationIterations = int(input('Number of generations or 0 to exit?: '))
        runForXGenerations(numberOfGenerationIterations, grid, counter)
    elif option == 2:
        grid = []
        value = 0
        print("Enter 0 or 1 one entry at a time, pressing enter after each entry:")
        for i in range(numberOfRows):
            a = []
            for j in range(numberOfColumns):
                try:
                    value = int(input("Enter value for grid entry {} {}: ".format(i, j)))
                except TypeError:
                    print("A non integer value was entered")
                    exit(1)
                a.append(value)
            grid.append(a)
        print('Generation ', counter)
        print(np.matrix(grid))
        numberOfGenerationIterations = int(input('Number of generations or 0 to exit?: '))
        runForXGenerations(numberOfGenerationIterations, grid, counter)
    elif option == 0:
        print('Program will exit')
        exit(1)
    else:
        print('Incorrect option selected. Try again')


def runForXGenerations(numberOfGenerationIterations, grid, counter):
    if numberOfGenerationIterations == 0:
        print('Program will exit')
        exit(1)
    else:
        while counter != numberOfGenerationIterations:
            counter += 1
            nextGenGrid = nextGenerationGrid(grid)
            print('Generation ', counter)
            print(np.matrix(nextGenGrid))
            grid = nextGenGrid
