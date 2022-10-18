import src


def menu() -> int:
    selectedOption = -1
    while selectedOption not in (0, 1, 2):
        print("____MENU_____")
        print("1: To generate a random Game of Life\n\
        2: Enter your own values for a Game of Life\n\
        0. Exit")
        try:
            selectedOption = int(input('Select Option: '))
            if selectedOption not in (0, 1, 2):
                print("An incorrect menu option was selected")
        except TypeError:
            print("A non integer value was entered")
        except ValueError:
            print("A non integer value was entered")
    return selectedOption


running = True
while running:
    menuOption = menu()
    if menuOption != 0:
        numberOfRows = int(input('Number of rows for the grid?: '))
        numberOfColumns = int(input('Number of columns for the grid?: '))
        src.runGameOfLife(numberOfRows, numberOfColumns, menuOption)
        print("Game of Life Complete")
        print("_____________________\n")
    else:
        print("Program will now exit")
        running = False
