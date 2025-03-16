import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load an csv file as DataFrame
    """
    try:
        if not path.lower().endswith(".csv"):
            raise AssertionError("Only .csv format is supported")
            return None
        ds = pd.read_csv(path)
    except (Exception, AssertionError) as error:
        print(f"Error : {error}")
        return None
    print(f"Loading dataset of dimensions {ds.shape}")
    return ds
