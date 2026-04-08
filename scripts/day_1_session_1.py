# Session 1: Numbers, Booleans, and Strings
# Live coding notes from Day 1, Session 1.
# Covers Python's scalar types: integers, floats, booleans, and strings.

# ============================================================
# Python's Object Model
# ============================================================

# Every value in Python is an object with an identity, a type, and a value.
# id() returns the memory address; type() returns the class.
x = 42
id(x)
type(x)

y = 13

# Arithmetic operators
x + y
x - y
x * y
x / y    # always returns a float (regular division)
x // y   # integer (floor) division: discards the remainder
x ** 2   # exponentiation (note: Python uses ** not ^)

# Name binding vs copying: b is bound to the same object as a.
# Rebinding a to 11 does not affect b.
a = 10
b = a
a = 11

# ============================================================
# Built-in Functions
# ============================================================

x = -10
abs(x)          # absolute value
max(x, y)
max(x, y, a, b)

# ============================================================
# Floats
# ============================================================

x = 42.0
type(x)

x + 11
x - 11
x * 2
x / 2
x // 2

x = 42.2323567
round(x, 3)

# Scientific notation: e means "times 10 to the power of"
1e6     # 1,000,000
2.2e3   # 2200.0
2.2e-3  # 0.0022

# Underscores in numeric literals are ignored — they are there for readability
1_000_000_00  # same as 100000000

# ============================================================
# Booleans
# ============================================================

True   # equivalent to R's TRUE
False  # equivalent to R's FALSE

x = True
type(x)

x = True
y = False

x and y
x or y
not x

# Comparison operators produce Boolean values
12 > 11
12 < 11
12 == 11  # equality test (== not =)

# ============================================================
# Strings
# ============================================================

x = 'this is a string, i.e. text'
y = "double quotation marks also work"
z = '''
multi-line strings use triple quotes
like this
'''

x = 'hello'
y = 'world'

x + y   # + means concatenate for strings
x * 3   # * means repeat
'h' in x   # membership test: is 'h' in the string?
len(x)     # number of characters

# String methods: called on the object using dot notation
x.upper()
x.index('h')   # position of the first 'h'
x.index('l')   # position of the first 'l'

# Indexing: Python uses zero-based indexing
x[0]    # first character
x[1]
x[4]    # last character (string has length 5, so index 4)
x[-1]   # last character (counting from the end)
x[-2]   # second to last

# Slicing: x[start:stop] extracts characters from start up to (not including) stop
x[0:2]
x[1:4]
