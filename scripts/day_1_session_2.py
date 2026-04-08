# Session 2: Collection Types
# Live coding notes from Day 1, Session 2.
# Covers lists, dictionaries, and tuples.

# ============================================================
# Lists
# ============================================================

x = [1, 2, 3]   # a list of three integers
type(x)
len(x)

# Lists can hold objects of any type, including mixed types
y = ['a', True, 42.0, 42]
type(y)

# Lists can contain other lists
z = [x, x, y]
type(z)
len(z)

# Indexing and slicing work the same as for strings
x[1]
y[0:3]
y[:3]   # omitting start defaults to 0

primes = [2, 3, 5, 7, 11, 13, 17]
primes[0:5]
primes[0:5:2]   # every second element from 0 up to (not including) 5
primes[:5]
primes[::2]     # every second element from start to end

# Nested (ragged) lists: inner lists can have different lengths
ragged = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10]]
ragged[0]
ragged[2]
ragged[1][0:3]    # chain two indexes to reach inside an inner list
# ragged[1, 0:3]  # does not work — Python lists do not support this syntax

sub_list = ragged[1]
sub_list[0:3]

# ============================================================
# List Operators and Methods
# ============================================================

x = [1, 2, 3]
y = [4, 5, 6]

x + y   # concatenation (not element-wise addition)
x * 5   # replication (not multiplication)

x.append(101)   # add a single element to the end
x

# Name binding vs copying: y = x makes both names refer to the same list.
# Modifying through one name is visible through the other.
x = [1, 2, 3]
y = x
x.append(42)

# To get an independent copy, use .copy()
x = [1, 2, 3]
y = x.copy()
x.append(42)   # y is unaffected

x.extend(['a', 'b', 'c'])   # add multiple elements from another sequence

# ============================================================
# Dictionaries
# ============================================================

# A dictionary maps keys to values; indexed by key, not by position
person = {'name': 'Mark', 'age': 25}
person['name']
person['age']

# Alternative construction using dict() with keyword arguments
person1 = dict(name='Jane', age=23)

# Views of the dictionary's contents
person.keys()
person.values()
person.items()

# Assigning to a new key adds it; assigning to an existing key updates it
person['country'] = 'Ireland'
person['country'] = 'England'   # overwrites the previous value

# update() adds or modifies multiple entries at once
person.update({'sex': 'male', 'height': 1.8})
person.update({'height': 1.7, 'surname': 'Andrews'})

# ============================================================
# Tuples
# ============================================================

# A tuple is an immutable ordered sequence — it cannot be modified after creation
point3d = (1.5, -3, 4.0)
point3d

# A list can be modified in place
point3d_list = [1.5, -3, 4.0]
point3d_list[0] = 'anything I want'
point3d_list

# A tuple cannot — this raises a TypeError
point3d[0] = 'anything I want'   # does not work

# To "prepend" a value you must construct a new tuple
('anything I want',) + point3d
