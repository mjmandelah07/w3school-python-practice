# NumPy Array Reshaping
# Reshaping arrays
# Reshaping means changing the shape of an array.
#
# The shape of an array is the number of elements in each dimension.
#
# By reshaping we can add or remove dimensions or change number of elements in each dimension.
#
# Reshape From 1-D to 2-D
# Example
# Convert the following 1-D array with 12 elements into a 2-D array.
#
# The outermost dimension will have 4 arrays, each with 3 elements:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print(newarr)

#  Reshape From 1-D to 3-D
# Example
# Convert the following 1-D array with 12 elements into a 3-D array.
#
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)
print(newarr)

# Returns Copy or View?
# Example
# Check if the returned array is a copy or a view:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

# Unknown Dimension
# You are allowed to have one "unknown" dimension.
#
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
#
# Pass -1 as the value, and NumPy will calculate this number for you.
#
# Example
# Convert 1D array with 8 elements to 3D array with 2x2 elements:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

# or Note: We can not pass -1 to more than one dimension.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, -1, 2)

print(newarr)

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
#
# We can use reshape(-1) to do this.
#
# Example
# Convert the array into a 1D array:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

newarr = arr.reshape(-1)

print(newarr)
