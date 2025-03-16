from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom():
    """
    This function loads an image, crops a portion of it
    (to simulate zooming in),converts the cropped portion to grayscale,
    and then displays the zoomed-in image.
    Steps:
        1. Loads the image from a file named "animal.jpeg".
        2. Verifies that the image was loaded successfully.
        3. Crops the image to a rectangular region defined by the
        coordinates (450, 100, 850, 500).
        4. Converts the cropped image into grayscale.
        5. Prints the new shape of the zoomed image.
        6. Displays the zoomed-in grayscale image using matplotlib.
        """
    try:
        image = (ft_load("animal.jpeg"))
        if isinstance(image, str) and image == "":
            raise AssertionError("Error Image not Loaded")
        else:
            print(image)
    except AssertionError as error:
        print(f"AssertionError: {error}")
        exit()
    zoomed_image = image[100:500, 450:850, :1]
    print(f"New shape after slicing: {np.array(zoomed_image).shape}")
    print(np.array(zoomed_image))
    plt.imshow(zoomed_image, cmap="gray")
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    zoom()
