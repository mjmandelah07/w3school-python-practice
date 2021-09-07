# Arrays
# Note: This page shows you how to use LISTS as ARRAYS, however,
# to work with arrays in Python you will have to import a library, like the NumPy library.
# Arrays are used to store multiple values in one single variable:
#
# Example
# Create an array containing car names:
#
cars = ["Ford", "Volvo", "BMW"]
print(cars)

# Access the Elements of an Array
# You refer to an array element by referring to the index number.
#
# Example
# Get the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)

# Modify the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"

print(cars)

# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
#
# Example
# Return the number of elements in the cars array:
cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
#
# Example
# Print each item in the cars array:
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# Adding Array Elements
# You can use the append() method to add an element to an array.
#
# Example
# Add one more element to the cars array:
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
#
# Example
# Delete the second element of the cars array:
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)

# you can also remove by using remove()
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")

print(cars)
