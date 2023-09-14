"""
Test goes here

"""

# from mylib.calculator import add
from main import generate_desc_stats

def test_main():
    m1, m2, s = generate_desc_stats("./resources/train.csv")
    ## test median
    assert m1["Survived"][0] == 0.0
    ## test mean
    assert round(m2["Survived"][0],6) == 0.383838
    ## test standard deviation
    assert round(s["Survived"][0],6) == 0.486592

if __name__ == "__main__":
    test_main()

