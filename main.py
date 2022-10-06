from src import gameOfLife

numberOfRows = int(input('Number of rows for the grid?: '))
numberOfColumns = int(input('Number of columns for the grid?: '))
print("____MENU_____")
print("1: To generate a random Game of Life for the grid specified above \n\
2: Enter your own values for the grid specified above")
option = int(input('Select Option: '))

gameOfLife.runGameOfLife(numberOfRows,numberOfColumns,option)
