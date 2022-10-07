# Coding Challenge - Game of Life

## Documentation

https://docs.google.com/document/d/1aFgHHfGyvDLc7AFuN_Ao7O4pcCetpZzGxY7DFhuflrU/edit?usp=sharing

## Instructions

Once the program is started, the user has to define the grid of cells. This has an upper limit of 100 to address performance issues which 
may arise due to a large dataset. Once the grid has been defined, the user has two options:
- Either generate a random grid of values or
- Fill in each cell within the grid manually

Following the creation of the grid and the addition of data, the initial generation
will be displayed. The user can select the number of generations/iterations of the 
game they wish to proceed through. These are displayed after each iteration to show the user
how the game they call life is developing.

## Run the program

To run the program, you run the following:
```
python3 __main__.py
```
or run the following from root
```
python3 moj-gurps-singh-challenge
```

## Running the tests

To run the tests, you can use either of the following from root:
```
python3 -m unittest discover (this will discover and run all Python unit tests)
python3 -m unittest test/test_gameOfLife.py
```

## References

https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
https://www.dataquest.io/blog/introduction-to-unit-tests-with-python/
https://stackoverflow.com/questions/448271/what-is-init-py-for
https://realpython.com/python-main-function/
https://www.techiediaries.com/python-unit-tests-github-actions/
https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python