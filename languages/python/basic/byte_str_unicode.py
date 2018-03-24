"""
Difference between byte str and unicode

Python3 has two types that represent sequence of chars
    1. Bytes, instnce contain raw 8 bit valu
    2. Str, instance contain unicode char (Python2 contain raw bit in str)
"""

# Convert unicode data to binary data
# use encode method in python string

str = "hello world" # unicode encoding by default python3
binary_data = str.encode() # Converted from unicode to binary


# Convert binary to unicod
x = b'Hello world' # binary data
x.decode() # converted to unicode
x.decode(encoding='utf-8')


# Write a function that convert the bytes to str

def to_str(bytes_or_str):
    if isinstace(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value

# Write a method that return the bytes of string

def to_bytes(bytes_or_string):
    if isinstance(bytes_or_string, string):
        return bytes_or_string.encode('utf-8') # encode to byte from unicode

    return bytes_or_string


# Are bytes and string instance are equal ?

print("Equal") if b'hello world' == 'hello world' else print("Not equal") # print not equal

# What is the default encoding of file in python3
# utf-8

# Can you add str and byte string?
# Not we can't, If str contain 7 bit ASCII char we can add otherwise not,
# by default str contain 8 bit ASCII
