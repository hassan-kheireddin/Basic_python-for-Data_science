from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def rotate():
    "it rotate the image in counterclockwise way by 3 loops"
    try:
        image = ft_load('animal.jpeg')
    except Exception as error:
        print(error)
        exit()
    image = image[100:500, 450:850, :1]
    print(f"The shape of image is: {image.shape}", end=" ")
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)
    row, col, color = image.shape
    rotated_image = np.zeros_like(image)
    for i in range(row):
        for j in range(col):
            for k in range(color):
                rotated_image[col-1-j, i, k] = image[i, j, k]
    print('New shape after Transpose: ', end='')
    print(f"({rotated_image.shape[0]}, {rotated_image.shape[1]})")
    rotated_image = np.squeeze(rotated_image)
    print(rotated_image)

    plt.imshow(rotated_image, cmap='gray')
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    rotate()
