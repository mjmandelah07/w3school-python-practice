# In python, variables can be created when you assign a value to it;
# example1
x = 5
y = "Hello World"

print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4  # (x is of type int)
x = "Sally"  # (x is of type str)

print(x)

# ANSWER= Sally         (override)


#                   CASTING
# If you want to specify the data type of a variable. this can be done with casting.
x = str(3)  # x will be '3'
x = int(3)  # x will be  3
x = float(3)  # x will be 3.0

#                GET THE TYPE
# You can get the type of a variable with the type() function.
x = 5
y = "John"
z = 3.0

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

#                   VARIABLES NAMES
# Variable can have a short name (like x and y) or a more descriptive name (age, carname, total volume)
#                    RULES
# 1.A variable name must start with a letter or underscore character(_)
#  2.A variable name cannnot start with a number
# 3.A variable name can only contain alpha_numeric characters and underscores(A-Z, 0-9, _)
# 4.Variable names are case sensitive(age, Age, and AGE are different characters)

# examples:
# Correct variable names;

#  myvar="John"
#   my_var="John"
#  _my_var="John"
#  myVar="John"
#  MyVar="John"
#  MYVAR="John"


# Incorrect variable names;
#   -myvar="John"
#   2var="John"
#   my var="John"


#                 MULTI WORDS VARIABLES NAMES
# Variable names with more than one words a=can be difficult to read;

#                 Camel case:
#  Each words except the first, start with capital
myVariableName = "John"
print(myVariableName)

# Pascal case:
# Each word starts with a capital letter
MyVariableName = "John"
print(MyVariableName)
#     Snake case
# Each word is separated by an underscore character
my_variable_name = "John"
print(my_variable_name)

# ASSIGN MULTIPLE VARIABLES
# Multiple variables to many values
x, y, z = "orange", "pink", "red"

print(x)
print(y)
print(z)

# One values to multiples variables
x = y = z = "orange"

print(x)
print(y)
print(z)

#       GLOBAL VARIABLES
# Variables created outside of a function are known as global variables

#  e.g1
#  create a variable outside the function;
x = "awesome"


def myfunc():
    print("python is" + x)


myfunc()

# e.g2
# create a variable inside a function, with the same name as the global variable
x = "awesome"


def myfunc():
    x = "fantastic"


print("python is" + x)

myfunc()
print("python is" + x)



#                The global keyword
# If you use the global keyword, the variable belong to the global scope.
# e.g
def myfunc():
    global x
    x = "fantastic"


myfunc()

print("python is" + x)

# Also use the global keyword if you want to change a global variable inside a function.
#  To change the value of a global variable inside a function refer to the variable by using the global keyword.

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("python is" + x)
