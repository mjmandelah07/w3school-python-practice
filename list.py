# Python Lists
# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:
# Example
this_list = ["apple", "banana", "cherry"]
print(this_list)

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
# Example
# Lists allow duplicate values:
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)

# List Length
# To determine how many items a list has, use the len() function:
# Example
# Print the number of items in the list:
this_list = ["apple", "banana", "cherry"]
print(len(this_list))

# List Items - Data Types
# List items can be of any data type:

# Example
# String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# A list can contain different data types:
# Example
# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
print(list1)

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':
# <class 'list'>
# Example
# What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
# Example
# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# Python - Access List Items
# Access Items
# List items are indexed and you can access them by referring to the index number:
# Example
# Print the second item of the list:
this_list = ["apple", "banana", "cherry"]
print(this_list[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Example
# Print the last item of the list:

this_list = ["apple", "banana", "cherry"]
print(this_list[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Example
# Return the third, fourth, and fifth item:

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])

# By leaving out the start value, the range will start at the first item:
# Example
# This example returns the items from the beginning to, but NOT including, "kiwi":

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[:4])

# By leaving out the end value, the range will go on to the end of the list:
# Example
# This example returns the items from "cherry" to the end:

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
# Example
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# Example
# Check if "apple" is present in the list:

this_list = ["apple", "banana", "cherry"]
if "apple" in this_list:
    print("Yes, 'apple' is in the fruits list")

    # Change Item Value
    # To change the value of a specific item, refer to the index number:
    # Example
    # Change the second item:

this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"
print(this_list)

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values,
#  and refer to the range of index numbers where you want to insert the new values:
# Example
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)

# If you insert more items than you replace, the new items will be inserted where you specified,
#  and the remaining items will move accordingly:
# Example
# Change the second value by replacing it with two new values:

this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list)

# If you insert less items than you replace, the new items will be inserted where you specified,
#  and the remaining items will move accordingly:
# Example
# Change the second and third value by replacing it with one value:

this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method
# The insert() method inserts an item at the specified index:
# Example
# Insert "watermelon" as the third item:

this_list = ["apple", "banana", "cherry"]
this_list.insert(3, "watermelon")
print(this_list)

# Python - Add List Items
# Append Items
# To add an item to the end of the list, use the append() method:
# Example
# Using the append() method to append an item:

this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list)

# Extend List
# To append elements from another list to the current list, use the extend() method.
# Example
# Add the elements of tropical to thislist:

this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Example
# Add elements of a tuple to a list:

this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)

# Python - Remove List Items

# Remove Specified Item
# The remove() method removes the specified item.
# Example
# Remove "banana":

this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)

# Remove Specified Index
# The pop() method removes the specified index.
# Example
# Remove the second item:
this_list = ["apple", "banana", "cherry"]
this_list.pop(1)
# print(this_list)

# If you do not specify the index, the pop() method removes the last item.
# Example
# Remove the last item:

this_list = ["apple", "banana", "cherry"]
this_list.pop()
print(this_list)

# The del keyword also removes the specified index:
# Example
# Remove the first item:

this_list = ["apple", "banana", "cherry"]
del this_list[0]
print(this_list)

# The del keyword can also delete the list completely.
# Example
# Delete the entire list:

this_list = ["apple", "banana", "cherry"]
del this_list

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# Example
# Clear the list content:

this_list = ["apple", "banana", "cherry"]
this_list.clear()
print(this_list)

# Python - Loop Lists
# Loop Through a List
# You can loop through the list items by using a for loop:
# Example
# Print all items in the list, one by one:

this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)

# Using a While Loop
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
# Remember to increase the index by 1 after each iteration.
# Example
# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


    # Looping Using List Comprehension
    # List Comprehension offers the shortest syntax for looping through lists:
    # Example
    # A short hand for loop that will print all items in a list:

this_list = ["apple", "banana", "cherry"]
[print(x) for x in this_list]



# Python - List Comprehension
# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# With list comprehension you can do all that with only one line of code:
# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)



# Python - List Methods
# List Methods
# Python has a set of built-in methods that you can use on lists.
#
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position

# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list