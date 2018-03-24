"""
How to write pip style code

sharing_common style make code collabarion simple.
"""
# 1. use white space instead of tabs.
# 2. Use 4 space 
# 3. Lines should be 79 chars in length.
# 4. Function and classes should seperated by two blank lines. 
# 5. protected variable should be be in _leading_underscore
# 6. Private variable should be __leading_underscore.
# 7. Class and Exception in capital lettrs
# 8. CONSTANT should be in all CAPS
# 9 instance method should use `self` as first argument
# 10. class method should use `cls` as first argument. 


# Prefered way

a = 1
b = 2

# Use this one
if a is not b:
    pass

# Avoid this one
if not a is b:
    pass 


# Use this one
a = 1
b = "" 
if not b: # Use this
    pass

# Avoid 
if b == "": # Avoid this
    pass # 

# Use pylint


