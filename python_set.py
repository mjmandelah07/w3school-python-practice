# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and un-indexed.

this_set = {"apple", "banana", "cherry"}
print(this_set)

# Duplicates Not Allowed
# Sets cannot have two items with the same value.
#
# Example
# Duplicate values will be ignored:

this_set = {"apple", "banana", "cherry", "apple"}
print(this_set)

# Get the Length of a Set
# To determine how many items a set has, use the len() method.
#
# Example
# Get the number of items in a set:
this_set = {"apple", "banana", "cherry"}
print(len(this_set))

# type()
# From Python's perspective, sets are defined as objects with the data type 'set'
my_set = {"apple", "banana", "cherry"}
print(type(my_set))

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
this_set = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(this_set)

# Access Items
# You cannot access items in a set by referring to an index or a key.
#
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.
this_set = {"apple", "banana", "cherry"}

for x in this_set:
    print(x)

# Example
# Check if "banana" is present in the set:
#
this_set = {"apple", "banana", "cherry"}

print("banana" in this_set)

# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
#
# To add one item to a set use the add() method.
#
# Example
# Add an item to a set, using the add() method:
this_set = {"apple", "banana", "cherry"}
this_set.add("orange")
print(this_set)

# Add Sets
# To add items from another set into the current set, use the update() method.
#
# Example
# Add elements from tropical into thisset:
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
this_set.update(tropical)
print(this_set)

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object
# (tuples, lists, dictionaries etc.).
# Example:
this_set = {"apple", "banana", "cherry"}
my_list = ["kiwi", "orange"]
this_set.update(my_list)
print(this_set)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
#
# Example
# Remove "banana" by using the remove() method:
this_set = {"apple", "banana", "cherry"}
this_set.remove("banana")
print(this_set)

# Loop Items
# You can loop through the set items by using a for loop:
#
# Example
# Loop through the set, and print the values:
this_set = {"apple", "banana", "cherry"}

for x in this_set:
    print(x)


# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
#
# Example
# Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)

print(x)


# The intersection() method will return a new set, that only contains the items that are present in both sets.
#
# Example
# Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#
# Example
# Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)

print(x)

# The symmetric_difference() method will return a new set,
# that contains only the elements that are NOT present in both sets.
# Example
# Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)

print(z)
