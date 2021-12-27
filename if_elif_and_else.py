#For Practice to show an example of how if, elif, and else statements works in Python.

from typing import cast


foo = 100

#structure of a if-elif-else statement. Note the == used as the comparison operator for equals
if foo == 30:
    foo = 'cat'
    
elif foo == 50:
    foo = 'dog'
    
else:
    foo = 'mouse'
    
#prints the current value of foo. Note python's dynamically typed language allows for values of different types to easily be assigned to the variable foo.
print(foo)













