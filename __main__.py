import src
#src is a module which can be imported as a module from any other python program
#in order to run anything in src from the command line, we can add a file like
#this then we can run the program from the terminal command like
# python3 python

#python looks for a file named main.py to start execution automatically
# if it doesnt find it it will throw an error else it will
#execute it and

#removes ambiguity among end user about entry point of program
#clean execution of code

numberOfRows = int(input('Number of rows for the grid?: '))
numberOfColumns = int(input('Number of columns for the grid?: '))
print("____MENU_____")
print("1: To generate a random Game of Life for the grid specified above \n\
2: Enter your own values for the grid specified above")
option = int(input('Select Option: '))

src.runGameOfLife(numberOfRows, numberOfColumns, option)
