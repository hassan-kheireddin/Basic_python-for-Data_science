import numpy as np


def give_bmi(height: list[int | float], weight:
             list[int | float]) -> list[int | float]:
    """
    Calculates the Body Mass Index (BMI) for a list of individuals.
    The BMI is computed using the formula:
    BMI = weight (kg) / (height (m) * height (m))
    Parameters:
    height (list[int | float]): A list of heights in meters.
    Each value must be greater than 0.
    weight (list[int | float]): A list of weights in kilograms
    Each value must be greater than 0.
    Returns:
        list[int | float]: A list containing the calculated BMI
        values.
    """
    list1 = np.array(height)
    list2 = np.array(weight)
    try:
        if len(height) != len(weight):
            raise AssertionError("The lists are not the same size")
        if len(list1[list1 <= 0]) != 0 or len(list2[list2 <= 0]) != 0:
            raise AssertionError("Value not valid !")
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return list()
    except Exception:
        print("the list are not int or float")
        return list()
    return list(list2 / (list1 * list1))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Compares a list of BMI values against a given limit.
    Parameters:bmi (list[int | float]): A list of BMI values.
                limit (int): The BMI threshold to compare against.
    Returns:
    list[bool]: A list of boolean values where each element indicates
    whether the corresponding BMI exceeds the limit."""
    list1 = np.array(bmi)
    return list(list1 > limit)
