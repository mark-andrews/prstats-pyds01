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
