# Session 4: Packages and NumPy
# Live coding notes from Day 2, Session 1.
# Covers Python's import system and the NumPy ndarray.

# ============================================================
# Packages and Imports
# ============================================================

# import loads a module and binds its name in the current namespace.
# Everything in the module is then accessible via the prefix.
import math
math.sqrt(16)
math.log(10)

# from ... import brings specific names directly into the global
# namespace so they can be used without a prefix.
from math import sqrt, log
sqrt(16)

# The standard convention for scientific Python is to import under
# a short alias. These aliases are universally recognised.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Avoid: from numpy import * floods the namespace and makes it
# impossible to tell where each name came from.

# ============================================================
# NumPy Arrays
# ============================================================

# NumPy's central object is the ndarray: a multidimensional array
# in which every element has the same data type. Operations are
# dispatched to compiled C code, making them far faster than
# equivalent Python loops.

x = [2, 3, 5, 7, 11, 13, 17]   # a plain Python list of integers
y = np.array(x)                  # convert to a 1D NumPy array
y

# Functions for creating arrays of standard forms
np.linspace(0, 1, 5)   # 5 evenly spaced values from 0 to 1 (like R's seq)
np.zeros(10)
np.arange(10)          # integers 0 to 9

# Three attributes describe the structure of an array
y.ndim    # number of dimensions
y.shape   # shape as a tuple
y.dtype   # data type of the elements

# A 2D array is created from a list of lists
m = np.array([[1, 2, 3], [4, 5, 6]])
m.ndim
m.shape   # (2, 3): two rows, three columns

# Ragged arrays are not supported; all rows must have the same length.
# np.array([[1, 2, 3], [4, 5, 6, 7]])   # raises ValueError

# 3D arrays follow the same pattern
y3 = np.array([[[1, 2, 3], [4, 5, 6]],
               [[1, 2, 3], [4, 5, 6]]])
y3.ndim
y3.shape

# ============================================================
# Indexing
# ============================================================

# 1D arrays are indexed exactly like lists: zero-based with slice notation.
y[0]
y[0:5]

# 2D arrays use a single pair of brackets with row and column separated
# by a comma. This is not possible with plain lists of lists.
m[0]         # entire first row
m[0][1]      # works, but creates an intermediate array
m[0, 1]      # preferred: row 0, column 1 in one step
m[0, 0:3:2]  # row 0, every second element from column 0 to 2

# Boolean indexing: a comparison returns a Boolean array of the same
# shape; that array then selects only the elements where it is True.
mask = y > 10
mask.dtype
y[y > 10]

# Compound conditions use & (and) and | (or), each sub-condition in parentheses.
y[(y >= 3) & (y <= 13)]

# ============================================================
# Element-wise Operations
# ============================================================

a = np.array([1, 2, 3])
b = np.array([6, 7, 8])

a + b   # element-wise addition; + means concatenation for plain lists
a * b   # element-wise multiplication
a / b

# NumPy ufuncs apply a function to every element and return an array.
# Python's math module only accepts scalars, not arrays.
# math.log(y)   # TypeError: raises an error on a NumPy array
np.log(y)       # element-wise natural log

# ============================================================
# Aggregations
# ============================================================

y.sum()     # method form
np.sum(y)   # function form; both give the same result

y.mean()
np.mean(y)

# For 2D arrays, axis=0 operates down the rows (one result per column)
# and axis=1 operates across the columns (one result per row).
m.mean(axis=0)
m.mean(axis=1)

# Centring each column by subtracting its mean is a one-liner.
m - m.mean(axis=0)

# ============================================================
# Broadcasting
# ============================================================

# A scalar is broadcast to every element.
y + 10
y * 2

# A 1D array is broadcast across every row of a 2D array, provided
# the number of elements matches the number of columns.
m + a   # a has shape (3,); m has shape (2, 3)

# ============================================================
# Reshaping and Transpose
# ============================================================

m.reshape(6, 1)   # reshape to a column vector
m.reshape(1, 6)   # reshape to a row vector
m.reshape(3, 2)   # 3 rows, 2 columns
m.T               # transpose: swap rows and columns

# ============================================================
# Matrix Operations
# ============================================================

a * b           # element-wise product (Hadamard product)
a @ b           # scalar dot product for 1D arrays
(a * b).sum()   # same result as the dot product above

m @ m.T         # matrix multiplication

np.linalg.eig(m @ m.T)   # eigenvalues and eigenvectors

# ============================================================
# Performance
# ============================================================

# NumPy's advantage comes from contiguous memory storage and compiled
# C/Fortran routines. The %timeit magic (Jupyter and IPython only)
# measures execution time by running a statement many times.

s = np.random.normal(size=1_000_000)
s_list = s.tolist()

%timeit np.sum(s)
%timeit sum(s_list)
