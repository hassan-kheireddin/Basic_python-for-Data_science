import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def display_image_with_title(image_array: np.ndarray, title: str) -> None:
    """
        display the colored image with the title
    """
    plt.imshow(image_array)
    plt.title(title)
    plt.axis('off')
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
        Inverts the color of the image received.
        by subtract white color from current color.
    """
    print(array)
    y, x, color = array.shape

    imageArray = Image.fromarray(array)

    for Y in range(y):
        for X in range(x):
            R, G, B = imageArray.getpixel((X, Y))
            R = 255 - R
            G = 255 - G
            B = 255 - B
            imageArray.putpixel((X, Y), (R, G, B))
    display_image_with_title(np.array(imageArray), "Invert")
    return np.array(imageArray)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
        Keeps only the red channel of the image.
        by Assign G and B zero and R still as it in (R,G,B)
    """
    print("The shape of image is:", array.shape)
    print(array)
    y, x, color = array.shape

    imageArray = Image.fromarray(array)

    for Y in range(y):
        for X in range(x):
            R, G, B = imageArray.getpixel((X, Y))
            imageArray.putpixel((X, Y), (R, 0, 0))
    display_image_with_title(np.array(imageArray), "Red")
    return np.array(imageArray)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
        Keeps only the green channel of the image.
        by Assign R and B zero and G still as it in (R,G,B)
    """
    print("The shape of image is:", array.shape)
    print(array)
    y, x, color = array.shape

    imageArray = Image.fromarray(array)

    for Y in range(y):
        for X in range(x):
            R, G, B = imageArray.getpixel((X, Y))
            imageArray.putpixel((X, Y), (0, G, 0))
    display_image_with_title(np.array(imageArray), "Green")
    return np.array(imageArray)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
        Keeps only the blue channel of the image.'
        by Assign R and G zero and B still as it in (R,G,B)
    """
    print("The shape of image is:", array.shape)
    print(array)
    y, x, color = array.shape

    imageArray = Image.fromarray(array)

    for Y in range(y):
        for X in range(x):
            R, G, B = imageArray.getpixel((X, Y))
            imageArray.putpixel((X, Y), (0, 0, B))
    display_image_with_title(np.array(imageArray), "blue")
    return np.array(imageArray)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
        Converts the image to greyscale.
    """
    print("The shape of image is:", array.shape)
    print(array)
    grey_ar = np.mean(array, axis=2, keepdims=True)
    grey_image = np.concatenate([grey_ar, grey_ar, grey_ar], axis=2)
    display_image_with_title(grey_image.astype(np.uint8), "Grey")
