#For Practice to show an example of how object comparison works in Python.

#change the value of foo and bar to see how each comparison answer changes.
foo = 'cat'
bar = 'dog'


def compare_object_values(foo, bar):
    print('Do foo and bar have the same value?\t', foo==bar)

def compare_if_same_object(foo, bar):
    print('Are foo and bar the same object?\t', foo is bar)

def compare_if_object_same_type():
    print('Are foo and bar of the same type?\t', type(foo) is type(bar))
    

print('foo = ', foo, '\tbar = ', bar, '\n')
compare_object_values(foo, bar)
compare_if_same_object(foo, bar)
compare_if_object_same_type()