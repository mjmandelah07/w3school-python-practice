# Dictionary
# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)

# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.
#
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#
# Example
# Print the "brand" value of the dictionary:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict["brand"])

# Dictionary length
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(len(this_dict))

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
#
# Example
# String, int, boolean, and list data types:
this_dict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(this_dict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
#
# Example
# Get the value of the "model" key:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = this_dict["model"]
print(x)

# OR
# There is also a method called get() that will give you the same result:
#
# Example
# Get the value of the "model" key:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = this_dict.get("model")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
#
# Example
# Get a list of the keys:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = this_dict.keys()
print(x)

# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change

# Get Values
# The values() method will return a list of all the values in the dictionary.
#
# Example
# Get a list of the values:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)

# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

# Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
#
# Example
# Get a list of the key:value pairs

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = this_dict.items()
print(x)

# Example
# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
#
# Example
# Check if "model" is present in the dictionary:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in this_dict:
    print("Yes, 'model' is one of the keys in the this_dict dictionary")

# Change Values
# You can change the value of a specific item by referring to its key name:
#
# Example
# Change the "year" to 2018:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

this_dict["year"] = 2018

print(this_dict)

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
#
# Example
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

this_dict["color"] = "red"
print(this_dict)

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument.
# Example
# Add a color item to the dictionary by using the update() method:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict.update({"color": "red"})

print(this_dict)

# Removing Items
# There are several methods to remove items from a dictionary:
#
# Example
# The pop() method removes the item with the specified key name:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict.pop("model")
print(this_dict)

# Example
# The del keyword removes the item with the specified key name:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del this_dict["model"]
print(this_dict)

# Example
# The del keyword can also delete the dictionary completely:
# del thisdict


# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in this_dict:
    print(x)

# print the values
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in this_dict:
    print(this_dict[x])

# Example
# You can also use the values() method to return values of a dictionary:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in this_dict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in this_dict.keys():
    print(x)

# Example
# Loop through both keys and values, by using the items() method:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in this_dict.items():
    print(x, y)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
#
# Example
# Create a dictionary that contain three dictionaries:
my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(my_family)

# Example
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

my_family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(my_family)
