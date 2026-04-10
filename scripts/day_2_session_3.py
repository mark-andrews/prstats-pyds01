# Session 6: Visualization and Statistical Modelling
# Live coding notes from Day 2, Session 3.
# Covers Matplotlib, Seaborn, plotnine, and statsmodels.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import ggplot, aes, geom_point
import statsmodels.formula.api as smf

# ============================================================
# Matplotlib
# ============================================================

# plt.plot draws a line plot. xlabel and ylabel label the axes.
x = np.linspace(0, 10, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.ylabel('sin(x)')
plt.xlabel('x')

plt.clf()   # clear the current figure before starting the next one

# plt.scatter draws a scatter plot. s controls the marker size.
x = np.random.normal(size=1_000)
y = 1.0 + 0.5 * x + np.random.normal(size=1_000)
plt.scatter(x, y, s=0.5)

plt.clf()

# ============================================================
# Seaborn
# ============================================================

# Seaborn wraps Matplotlib with functions that accept a DataFrame
# and column names as strings, so there is no need to extract arrays.
# The tips dataset ships with the library.
tips = sns.load_dataset('tips')

# histplot draws a histogram.
sns.histplot(data=tips, x='total_bill')

plt.clf()

# The hue argument splits the distribution by a categorical variable.
sns.histplot(data=tips, x='total_bill', hue='time')

plt.clf()

# scatterplot maps two continuous variables to position.
sns.scatterplot(data=tips, x='total_bill', y='tip')

plt.clf()

# Adding hue colours the points by a categorical variable.
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')

plt.clf()

# ============================================================
# plotnine
# ============================================================

# plotnine is a Python implementation of the grammar of graphics,
# closely mirroring R's ggplot2. A plot is built by adding layers
# with +. Column names are passed as strings rather than bare names.
(
    ggplot(tips, aes(x='total_bill', y='tip'))
    + geom_point()
)

# ============================================================
# Statistical Modelling
# ============================================================

# statsmodels provides a formula API similar to R's modelling syntax.
# smf.ols fits ordinary least squares regression. The formula string
# uses ~ to separate the response from the predictors.

# Linear regression: tip ~ total_bill
# Equivalent to R's: lm(tip ~ total_bill, data = tips)
m = smf.ols('tip ~ total_bill', data=tips)
result = m.fit()
print(result.summary())

result.params       # estimated coefficients
result.pvalues      # p-values for the coefficients
result.f_pvalue     # p-value for the overall model fit
result.conf_int()   # confidence intervals for the coefficients

# Logistic regression follows the same interface via smf.logit.
affairs = pd.read_csv(
    'https://raw.githubusercontent.com/mark-andrews/prstats-pyds01/refs/heads/main/site/data/affairs.csv'
)
affairs2 = affairs.assign(had_affair=(affairs['affairs'] > 0).astype(int))

m2 = smf.logit('had_affair ~ age + gender', data=affairs2)
result2 = m2.fit()
print(result2.summary())

result2.params
result2.conf_int()
