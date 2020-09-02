"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open("foo.txt", "r")

lines = f.readlines()
for line in lines:
    print(line)

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

x = open("bar.txt", "w")
A = ["This is a line \n", "This is another line \n", "this is another line still \n"]

x.writelines(A)
x.close()

y = open("bar.txt")

lines = y.readlines()
for line in lines:
    print(line)

x.close()

