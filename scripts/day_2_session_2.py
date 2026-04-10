# Session 5: Pandas
# Live coding notes from Day 2, Session 2.
# Covers DataFrames: loading data, selecting columns, renaming columns,
# filtering rows, and adding new columns.

import pandas as pd

# ============================================================
# DataFrames
# ============================================================

# A DataFrame is a two-dimensional table of columns, each sharing a
# common index. The quickest way to create a small one by hand is from
# a dictionary of lists.
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['A', 'B', 'C']})
df

# In practice, data almost always comes from a file or URL.
affairs = pd.read_csv(
    'https://raw.githubusercontent.com/mark-andrews/prstats-pyds01/refs/heads/main/site/data/affairs.csv'
)
affairs.head()

# ============================================================
# Selecting Columns
# ============================================================

# A single name in square brackets returns a Series.
affairs['age']

# A list of names returns a DataFrame with only those columns.
affairs[['age', 'gender', 'children']]

# drop removes named columns.
affairs.drop(columns=['age', 'gender'])

# filter selects columns by name pattern. regex='^y' matches columns
# whose names start with 'y'. This operates on column names, not values.
affairs.filter(regex='^y')

# loc uses labels; iloc uses integer positions.
affairs.loc[:, ['age', 'gender', 'children']]
affairs.loc[:, 'age':'education']   # all columns from 'age' to 'education', inclusive
affairs.iloc[:, 2:5]                # columns at positions 2, 3, and 4
affairs.iloc[10:15, 2:5]           # rows 10 to 14, columns 2 to 4

# ============================================================
# Renaming Columns
# ============================================================

# rename takes a dictionary mapping old names to new names.
# Only the names in the dictionary are changed.
affairs.rename(columns={'gender': 'sex'})

rename_map = dict(gender='sex', age='Age')
affairs.rename(columns=rename_map)

# ============================================================
# Filtering Rows
# ============================================================

# A comparison on a column returns a Boolean Series.
# That Series indexes the DataFrame to keep only the matching rows.
affairs[affairs['gender'] == 'male']

# query accepts a condition as a string, which is often easier to read
# for complex expressions.
affairs.query("gender == 'male'")

# Compound conditions work in both styles.
affairs[(affairs['gender'] == 'male') & (affairs['age'] <= 25)]
affairs.query("gender == 'male' and age <= 25")

# A variable defined outside the query string is referenced with @.
min_age = 25
affairs.query("gender == 'male' and age <= @min_age")

# ============================================================
# Adding Columns
# ============================================================

# assign returns a new DataFrame with additional or modified columns.
# The original DataFrame is never modified.
affairs.assign(happy=affairs['rating'] >= 3)
