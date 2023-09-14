# IDS 706 Data Engineering Week 3 Mini Project

## Template

1. First thing to do on launch is to open a new shell and verify virtualenv is sourced.

Things included are:

* `Makefile`

* `Pytest`

* `pandas`

* `Ruff`:  

Run `make lint` which runs `ruff check`.  You can find out more info on [Ruff here](https://github.com/astral-sh/ruff).

* `Dockerfile`

* `GitHub copilot`

* `jupyter` and `ipython` 

* A base set of libraries for devops and web

* `githubactions`


## Descriptive Statistics using Python Polars

1. Read the csv file at `./resources/train.csv` using `polars.read_csv()` function

2. Generated sumamry statistics for variable `Survived` in the `Titanic` dataset using `.median()`, `.mean()`, `.std()` function. The result is as follow:

![Summary_stats](./resources/desc_stats.png)

3. Generated histogram for variable `Survived` in the `Titanic` dataset using `matplotlib.pyplot`.



## References

[Professor Noah's ruff template](https://github.com/nogibjj/python-ruff-template)



