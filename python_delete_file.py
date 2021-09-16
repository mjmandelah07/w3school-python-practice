# Python Delete File
# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
#
# Example
# Remove the file "demofile.txt":
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("Myfile  does not exist")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example
# Check if file exists, then delete it:
import os
if os.path.exists("myfile2.txt"):
    os.remove("myfile2.txt")
else:
    print("Myfile2  does not exist")

import os
if os.path.exists("myfile3.txt"):
    os.remove("myfile3.txt")
else:
    print("Myfile3 does not exist")


#
