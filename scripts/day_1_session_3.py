# Session 3: Iteration, Comprehensions, and Functions
# Live coding notes from Day 1, Session 3.
# Covers for loops, while loops, list and dictionary comprehensions, and functions.

# ============================================================
# For Loops
# ============================================================

fruits = ['apple', 'orange', 'cherry']

# Iterate directly over elements — the loop variable takes each value in turn
for fruit in fruits:
    print(fruit.upper())

# A common pattern: build a new list by appending inside a loop
X = []
for fruit in fruits:
    X.append(fruit.upper())

# Summing a list manually with a loop
primes = [2, 3, 5, 7, 11, 13, 17]
s = 0
for prime in primes:
    s = s + prime

sum(primes)   # built-in equivalent of the loop above

# ============================================================
# While Loops
# ============================================================

# A while loop repeats as long as a condition holds
s = 0
while s < 5:
    s = s + 1
    print(s)

# ============================================================
# Comprehensions
# ============================================================

# A list comprehension is a concise alternative to the append-in-a-loop pattern above
[fruit.upper() for fruit in fruits]

# A dictionary comprehension produces a dictionary
{fruit: fruit.upper() for fruit in fruits}

# Equivalent loop-based version of the dictionary comprehension above
X = {}
for fruit in fruits:
    X[fruit] = fruit.upper()

# ============================================================
# Functions
# ============================================================

# Define a function with def; return sends back the result to the caller
def mean(x):
    return sum(x) / len(x)

result = mean(primes)

# For comparison, the equivalent function definition in R:
# mean2 <- function(x) {
#     sum(x) / length(x)
# }

# ============================================================
# Conditionals
# ============================================================

# An if statement executes a block only when the condition is true.
# elif provides additional cases; else catches everything else.
x = -42
if x > 0:
    result = 'positive'
elif x == 0:
    result = 'zero'
else:
    result = 'negative'

# Conditionals become natural inside functions, where different
# inputs can follow different paths and return different values.
def classify(x):
    if x > 0:
        return 'positive'
    elif x == 0:
        return 'zero'
    else:
        return 'negative'

classify(10)
classify(-3)
classify(0)

# ============================================================
# Classes
# ============================================================

# Everything in Python is an object, and every object is an instance
# of a class. You can define your own classes to bundle related data
# and operations into a single object.

# Without a class, data and functions that belong together are unrelated.
def circumference(r):
    return 3.14 * r * 2

def area(r):
    return 3.14 * r ** 2

# A class groups them. The simplest form has a class attribute shared
# by all instances.
class Circle:
    r = 2.0

circle_1 = Circle()   # create an instance of the class
circle_2 = Circle()   # create another independent instance

id(circle_1)
id(circle_2)

type(circle_1)
isinstance(circle_1, Circle)

# An attribute can be set on an individual instance, overriding the
# class-level value for that instance only.
circle_1.r = 11

# Methods are functions defined inside the class. The first parameter,
# self, refers to the instance the method is called on.
class Circle:
    r = 2.0

    def circumference(self):
        return 3.14 * self.r * 2

    def area(self):
        return 3.14 * self.r ** 2

circle_3 = Circle()
circle_3.circumference()
circle_3.area()

circle_3.r = 5.5   # update the radius
circle_3.area()

# The __init__ method is called automatically when an instance is created.
# It sets per-instance attributes so each circle can have its own radius.
class Circle:

    def __init__(self, r):
        self.r = r

    def circumference(self):
        return 3.14 * self.r * 2

    def area(self):
        return 3.14 * self.r ** 2

c1 = Circle(r=2.56)
c2 = Circle(r=10.0)

c1.r
c1.area()
c2.area()

isinstance(c1, Circle)
