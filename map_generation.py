from PIL import Image
import numpy as np


# Transforms image to txt-file of binary numbers and writes it
# Source code: https://dev.to/anuragrana/generating-ascii-art-from-colored-image-using-python-4ace
def text_file_map(filename='Data/map.jpg', resolution=360):

    # pass the image as command line argument
    img = Image.open(filename)

    # convert image to greyscale format
    img = img.convert('L')

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_width = resolution
    new_height = aspect_ratio * new_width * 1
    img = img.resize((new_width, int(new_height)))

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ['1', '0']
    new_pixels = [chars[pixel//128] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)

    # write to a text file.
    with open("Data/map.txt", "w") as f:
        f.write(ascii_image)

    return None


# Transforms txt-map to np.array
def array_map(filename='Data/map.txt'):

    with open(filename, 'r') as f:
        map = []

        for line in f.readlines():
            new_line = []

            for chars in line:
                if chars != '\n':
                    chars = int(chars)
                    new_line.append(chars)

            map.append(new_line)

        map = np.array(map, dtype=object)

        # Change '1' to 'None' due to needs of path_finder
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    map[i][j] == None

    return map.tolist()
