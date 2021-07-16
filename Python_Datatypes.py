# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type:	      str
# Numeric Types:	  int, float, complex
# Sequence Types:   list, tuple, range
# Mapping Type:	  dict
# Set Types:	      set, frozenset
# Boolean Type:	  bool
# Binary Types:	  bytes, bytearray, memoryview

# Getting the Data Type
# You can get the data type of any object by using the type() function:

# Example
# Print the data type of the variable x:

x = 5
print(type(x))

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

# examples
x = "Hello World"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = range(6)
print(type(x))

x = {"name": "John", "age": 36}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

#Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

#Example
x = str("Hello World")
print(type(x))

x = int(20)
print(type(x))

x = float(20.5)
print(type(x))

x = complex(1j)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(type(x))

x = range(6)
print(type(x))

x = dict(name="John", age=36)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(type(x))

x = bool(5)
print(type(x))

x = bytes(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))
