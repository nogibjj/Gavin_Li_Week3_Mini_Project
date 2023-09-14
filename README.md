[![CI](https://github.com/nogibjj/Gavin_Li_Week3_Mini_Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Gavin_Li_Week3_Mini_Project/actions/workflows/cicd.yml)

# IDS 706 Data Engineering Week 3 Mini Project

## Template

For this week's mini project, I used a template that is slightly different than the one used for the first two weeks.

This template lints code using `ruff` instead of `pylint`, which was used in the previous two mini projects.

## Descriptive Statistics using Python Polars

1. Read the csv file at `./resources/train.csv` using `polars.read_csv()` function

2. Generated sumamry statistics for variable `Survived` in the `Titanic` dataset using `.median()`, `.mean()`, `.std()` function. The result is as follow:

![Summary_stats](./resources/desc_stats.png)

3. Generated histogram for variable `Survived` in the `Titanic` dataset using `matplotlib.pyplot`.

![Histogram](./resources/hist.png)

## References

[Professor Noah's ruff template](https://github.com/nogibjj/python-ruff-template)



