import pyspark.pandas as pd
from os import environ as env


def main():
    # initializing spark session
    # pyspark.pandas test
    data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
    df = pd.DataFrame(data)
    print(df.head())


if __name__ == "__main__":
    main()
