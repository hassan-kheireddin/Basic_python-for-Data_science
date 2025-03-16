import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a given 2D list (family) using NumPy and prints the
    shape before and after slicing.
    Parameters:
    -----------
    family : list
        A 2D list (list of lists) representing a matrix.
    start : int
        The starting index for slicing.
    end : int
        The ending index for slicing.
    Returns:
    --------
    A new 2D list (list of lists) that
    represents the sliced portion of the original list.
    """
    try:
        if not isinstance(family, list) or not isinstance(start, int) \
                or not isinstance(end, int):
            raise AssertionError("Bad Parameter")
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return list()
    try:
        temp = np.array(family)
    except Exception:
        print("Error size list")
        return list()

    result = temp[start: end]
    print(f"My shape is : {temp.shape}")
    print(f"My new shape is : {result.shape}")
    return result.tolist()
