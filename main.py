"""
Main cli or app entry point
"""

import polars as pl
import matplotlib.pyplot as plt

def generate_desc_stats(path: "str"):
    df = pl.read_csv(path, ignore_errors=True)
    # print(df)
    return df.median(), df.mean(), df.std()

def generate_visual_for_titanic():
    df = pl.read_csv("./resources/train.csv", ignore_errors=True)
    plt.hist(df.get_column("Survived"))
    plt.title("Histogram of Survived")
    plt.xlabel("Survived")
    plt.ylabel("Count")
    plt.show()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    # add_cli()
    path = "./resources/train.csv"
    print(generate_desc_stats(path))
    generate_visual_for_titanic()

