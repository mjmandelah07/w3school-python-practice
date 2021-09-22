# NumPy Tutorial
# NumPy is a Python library.
# NumPy is used for working with arrays.
# NumPy is short for "Numerical Python".
# Learning by Examples
# In our "Try it Yourself" editor, you can use the NumPy module, and modify the code to see the result.
#
# Example
# Create a NumPy array:
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

# NumPy as np
# NumPy is usually imported under the np alias.
#
# alias: In Python alias are an alternate name for referring to the same thing.
#
# Create an alias with the as keyword while importing:
#
# import numpy as np
# Now the NumPy package can be referred to as np instead of numpy.
#
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Checking NumPy Version
# The version string is stored under __version__ attribute.
#
# Example
import numpy as np

print(np.__version__)

