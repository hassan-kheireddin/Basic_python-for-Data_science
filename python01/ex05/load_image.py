import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    You need to write a function that loads an image, prints its format,
    and its pixels content in RGB format.
    You have to handle, at least, JPG and JPEG format.
    You need to handle any error with a clear error message
    Parameters
    path (str): The path to the image file to be loaded.
    Returns:
    np.ndarray: A NumPy array representing the loaded image.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
    except AssertionError as error:
        print(f"AssertionError : {error}")
        return 0

    try:
        input = Image.open(path)
        input = np.array(input)
        print(f"The shape of image is: {input.shape}")
        return input
    except Exception:
        print(f"{Exception.__name__} : File no present")
        return 0
