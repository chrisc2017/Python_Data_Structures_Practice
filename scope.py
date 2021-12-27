#For Practice to show an example of how scope works in Python.

foo = 50
bar = 90

def local_scope_test():
    foo = 2 #foo is still locally defined
    bar = 7 #bar is still locally defined
    
    print("Local Scope Test - defined variables within the function:")
    print('Local  foo = ', foo, '\tLocal  bar = ', bar, '')
    print_global_values()
    
def global_scope_test():
    global foo
    foo = 80 #redefining the value of global foo
    bar = 7 #bar is still locally defined
    
    print("Global Scope Test - referenced global foo and defined bar locally:")
    print('Local  foo = ', foo, '\tLocal  bar = ', bar, '')
    print_global_values()
    
#Only prints the global variables
def print_global_values():
    print('Global foo = ', foo, '\tGlobal bar = ', bar, '\n')
    
#run each test
print('Global values before testing:\tfoo = ', foo, '\tGlobal bar = ', bar, '\n')
local_scope_test()
global_scope_test()