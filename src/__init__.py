from .gameOfLife import runGameOfLife

'''
A Python module is simply a single python file or an organised collection of python modules

If we use init.py files, we are making ti easier to develop larger Python projects

Provides a mechanism to group seperate python scripts into a single importable module

If we did not have this file, we could only import files if they are in the current directory
that whatever script we are in is running from

If we add a blank file, we can then refer to the folder.pyfile.method to access the method

If we add the imports like above, we can use folder.method to retrieve the method

Note the . bnefore the module as since Python 3, relative importing got more strict
https://stackoverflow.com/questions/12172791/changes-in-import-statement-python3?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

I allows us to treat a directory as if it was a python module

python -v -m my_scriptname.py is good for debugging as we can check the output to see exactly
where the modules are imported from

'''