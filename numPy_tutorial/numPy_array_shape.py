# NumPy Array Shape
# Shape of an Array
# The shape of an array is the number of elements in each dimension.
#
# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a
#  tuple with each index having the number of corresponding elements.
# Example
# Print the shape of a 2-D array:
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

# Example
# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4
# and verify that last dimension has value 4:
import numpy as np

arr = np.array([1,2,3,4], ndmin=5)

print(arr)
print("Shape of the array:", arr.shape)

