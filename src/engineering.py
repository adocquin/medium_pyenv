"Feature engineering functions"
import pandas as pd


def target_mean_encoding(data: pd.DataFrame, target: pd.Series, column: str):
    """
    Target mean encoding for categorical variables.

    Args:
        data (pd.DataFrame): Dataframe containing the column to be encoded.
        target (pd.Series): Series containing the target variable.
        column (str): Name of the column to be encoded.

    Returns:
        pd.Series: Encoded column.
    """
    return data[column].map(target.groupby(data[column]).mean())


if __name__ == "__main__":
    dataframe: pd.DataFrame = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    print(
        target_mean_encoding(
            dataframe,
            dataframe["b"],
            "a",
        )
    )
