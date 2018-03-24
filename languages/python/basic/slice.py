"""
slice can be implemented in any class by implementing
__getitem__
__setitem__
""" 

mystring = "hello world"

mystring[::-1] # reverse the string.
mystring[1:3] # get index item 1, and 2 it exclude last item.

# slicing won't modify the original data structure.

# Expand the list using slice?
lst = [1,2,3]
sublist = [4,5,6]
lst[1:1] = sublist # result [1,4,5,6,2,3], expand the list at position1

# Copy the list using slice operator
lst = sublist[:]
