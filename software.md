# Software Requirements and Installation

Setting up Python for data science is more involved than installing a single application. 
There are many valid combinations of tools, and this document describes the most common approaches.
All software listed here is free and open-source.
Python 3.9 or later is required.

## Choosing an Interactive Environment

For data analysis work, you need an environment that lets you run Python interactively — executing code and seeing results immediately.
The minimal Python console that ships with Python itself is workable but frustrating; you want something better.
There are two main categories of tool worth considering: a data science IDE, or Jupyter.

### Option 1: An IDE

An integrated development environment gives you an editor, an interactive console, a variable explorer, and a plot viewer in one application.
My recommendation is [Positron](https://positron.posit.co/), an open-source data science IDE developed by Posit, the company behind RStudio.
It is designed specifically for interactive data work in Python and R, and will feel immediately familiar to anyone coming from RStudio.

Other IDEs are equally valid if you already have a preference:

- [Spyder](https://www.spyder-ide.org/) is another data science-oriented option.
- [VS Code](https://code.visualstudio.com/) with the Python extension is widely used.
- [PyCharm](https://www.jetbrains.com/pycharm/) is a full-featured option popular in professional settings.

### Option 2: Jupyter

Jupyter is a browser-based environment in which you write and run Python inside a notebook: a document that interleaves code cells, their output, and prose.
It is widely used in data science and scientific computing and works well for the kind of exploratory work this course involves.

There are three main ways to use Jupyter:

- **Jupyter Notebook** is the original interface — simple, lightweight, and straightforward.
- **JupyterLab** is its modern successor, offering a more complete environment with a file browser, multiple panels, and a terminal.

For a local installation, JupyterLab is the better choice; instructions are at [jupyter.org/install](https://jupyter.org/install).

**Google Colab** is a cloud-hosted Jupyter environment at [colab.research.google.com](https://colab.research.google.com).
It runs entirely in the browser, requires no local installation, and is the simplest way to get started if you want to avoid setting anything up on your own machine.
It is not a limited or cut-down Python environment — it provides a full Jupyter notebook running on Google's servers, with all common data science packages already available.

## Required Packages

The course requires the following Python packages:

```
numpy  pandas  matplotlib  seaborn  plotnine  statsmodels  jupyter  ipykernel
```

Install them with pip:

```bash
pip install numpy pandas matplotlib seaborn plotnine statsmodels jupyter ipykernel
```

It is strongly recommended to install these into a virtual environment rather than into your system Python installation (see below).
If you are using Google Colab, these packages are already available and no installation is needed.

## Virtual Environments

A virtual environment is an isolated Python installation scoped to a specific project.
It prevents packages installed for one project from conflicting with those of another, and keeps your system Python clean.
This is standard practice in Python and worth learning from the start.

### Using venv (recommended)

Python's built-in `venv` module requires no additional installation:

```bash
# Create a virtual environment in a folder named 'env'
python -m venv env

# Activate it — macOS and Linux
source env/bin/activate

# Activate it — Windows
env\Scripts\activate

# Install the required packages
pip install numpy pandas matplotlib seaborn plotnine statsmodels jupyter ipykernel

# Deactivate when finished
deactivate
```

Once the environment is activated, your terminal prompt will show its name, and all `pip install` commands will install into it rather than system-wide.
In Positron or VS Code, you select the virtual environment as your Python interpreter and the IDE handles activation for you.

### Using conda

Conda is an alternative package and environment manager that is popular in the scientific Python community.
If you already have Anaconda or Miniconda installed, you can create an environment as follows:

```bash
conda create -n pyds python=3.11
conda activate pyds
pip install numpy pandas matplotlib seaborn plotnine statsmodels jupyter ipykernel
```

Conda is not required for this course; `venv` and `pip` work perfectly well and involve fewer moving parts.
It is mentioned here because many participants will already have Anaconda installed.

## Suggested Setup

The simplest local setup that covers everything needed for this course:

1. Install Python 3.9 or later from [python.org/downloads](https://www.python.org/downloads/)
2. Create a virtual environment: `python -m venv env` and activate it
3. Install the packages: `pip install numpy pandas matplotlib seaborn plotnine statsmodels jupyter ipykernel`
4. Install [Positron](https://positron.posit.co/) and point it at the virtual environment as your interpreter

Alternatively, install JupyterLab (`pip install jupyterlab`) and launch it with `jupyter lab`.
Or use Google Colab with no local installation at all.

There is no single correct way to do this.
The combination of Python, a virtual environment, a handful of packages, and a comfortable editor covers all possible approaches.
