"""
Main cli or app entry point
"""

import polars as pl

def generate_desc_stats(path: "str"):
    df = pl.read_csv(path)
    # print(df)
    return df.median(), df.mean(), df.std()



if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    # add_cli()
    path = "./resources/train.csv"
    print(generate_desc_stats(path))
