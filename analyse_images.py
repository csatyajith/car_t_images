import glob

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def get_images():
    for filename in glob.glob("/Users/csatyajith/Datasets/dongfang/data/*642*.tif"):
        print(filename)
        im = Image.open(filename)
        im_array = np.array(im)
        yield im_array


def print_extremes(im_array):
    one_d = im_array.flatten()
    print(min(one_d), max(one_d))


def plot_histogram(flattened_im_arr):
    plt.hist(flattened_im_arr, range(0, 255))
    plt.show()


if __name__ == '__main__':
    p = 0
    for j, image in enumerate(get_images()):
        if j < p:
            continue
        flat_img_arr = image.flatten()
        print_extremes(image)
        # plot_histogram(flat_img_arr)

        intensity_count = 0
        for pixel in flat_img_arr:
            if pixel > 150:
                intensity_count += 1

        for i in range(999900, 1000000):
            print("{} percentile {}".format(i/10000, np.percentile(flat_img_arr, i/10000)))

        break
