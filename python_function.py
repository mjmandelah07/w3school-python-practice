# Python Functions
# A function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:
#
# Example:
def my_function():
    print("Hello from a function")


# Calling a Function
# To call a function, use the function name followed by parenthesis:
#
# Example
def my_function():
    print("Hello fron a function")


my_function()


# Arguments
# Information can be passed into functions as arguments.
#
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want,
# just separate them with a comma.
# The following example has a function with one argument (fname).
# When the function is called, we pass along a first name,
# which is used inside the function to print the full name:
# Example
def my_function(fname):
    print(fname + " aramide")


my_function("Moji")
my_function("Dorcas")
my_function("Abigeal")
my_function("Lydia")


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
#
# From a function's perspective:
#
# A parameter is the variable listed inside the parentheses in the function definition.
#
# An argument is the value that is sent to the function when it is called.
#
# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments,
# you have to call the function with 2 arguments, not more, and not less.
# Example
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Mojisola", "Aramide")


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
#
# Example
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
# You can also send arguments with the key = value syntax.
#
# This way the order of the arguments does not matter.
#
# Example
def my_function(child1, child2, child3):
    print("Our first child name is " + child1)


my_function(child1="Mojisola", child2="Dorcas", child3="Abigeal")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
#
# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kids):
    print("His last name is " + kids["lname"])


my_function(fname="mojisola", lname="aramide")


# Default Parameter Value
# The following example shows how to use a default parameter value.
#
# If we call the function without argument, it uses the default value:
#
# Example
def my_function(country="Sweden"):
    print("Im from " + country)


my_function("Norway")
my_function()
my_function("America")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
#  and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
#
# Example
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values
# To let a function return a value, use the return statement:
#
# Example
def my_function(x):
    return 5*x


print(my_function(3))
print(my_function(5))

