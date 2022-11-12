import random
import math
from PIL import Image


# takes an image and rearranges the pixels in ascending order from top to bottom and saves it as a
# new image
def prism_hash(image, new_name):
    # open the image
    img = Image.open(image)
    # get the width and height of the image
    width, height = img.size
    # create a new image with the same width and height
    new_img = Image.new('RGB', (width, height))
    # create a list of all the pixels in the image
    pixels = list(img.getdata())
    # sort the pixels in ascending order from 0 to 255
    pixels.sort()
    # put the pixels in the new image
    new_img.putdata(pixels)
    # save the new image
    new_img.save(f'{new_name}.png')


# takes two images and counts the number of times each color appears in both images and if they are the same return
# true else return false
def compare_img_hash(image, hash_image):
    # open the images
    img1 = Image.open(image)
    img2 = Image.open(hash_image)

    # create a list of all the pixels in the images
    pixels1 = list(img1.getdata())
    pixels2 = list(img2.getdata())
    # create a dictionary of the colors in the images
    colors1 = {}
    colors2 = {}

    for pixel in pixels1:
        # get the red, green, and blue values of the pixel
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        # create a string of the rgb values
        rgb = f'{red}, {green}, {blue}'
        # if the color is in the dictionary
        if rgb in colors1:
            # add one to the count of the color
            colors1[rgb] += 1
        # else
        else:
            # add the color to the dictionary with a count of 1
            colors1[rgb] = 1

    for pixel in pixels2:
        # get the red, green, and blue values of the pixel
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        # create a string of the rgb values
        rgb = f'{red}, {green}, {blue}'
        # if the color is in the dictionary
        if rgb in colors2:
            # add one to the count of the color
            colors2[rgb] += 1
        # else
        else:
            # add the color to the dictionary with a count of 1
            colors2[rgb] = 1
    # if the colors in the images are the same
    if colors1 == colors2:
        return True
    else:
        return False

# takes a string of data and encrypts it into an image, saves the image,
# and returns the seed of where the data is in the rgb spectrum of the image. the seed is needed to decrypt the image
def prism(string: str, new_name: str):

    shift1, shift2 = generate_shifts()

    # create a list of the characters in the string
    characters = list(string)
    characters.insert(0, 'ÿ')
    characters.append('ÿ')
    char_len = len(characters)

    width = round(math.sqrt(len(characters))) + 1
    height = round(math.sqrt(len(characters))) + 1

    sequence = generate_seed(char_len)

    new_img = Image.new('RGB', (width, height))

    pixels = []
    count = 0
    while count != char_len:

        for character in characters:

            # get the ascii value of the character
            ascii_value = ord(character)

            if sequence[count] == 1:
                # add the pixel to the list of pixels
                pixels.append((ascii_value, shift1, shift2))
                count += 1
            elif sequence[count] == 2:
                # add the pixel to the list of pixels
                pixels.append((shift1, ascii_value, shift2))
                count += 1
            elif sequence[count] == 3:
                # add the pixel to the list of pixels
                pixels.append((shift1, shift2, ascii_value))
                count += 1
    # put the pixels in the new image
    new_img.putdata(pixels)
    # save the new image
    new_img.save(f'{new_name}.png')
    return sequence


# takes an image and returns a string of the characters in the image based on the sequence seed
def prism_decrypt(image, sequence):
    # open the image
    img = Image.open(image)
    # create a list of all the pixels in the image
    pixels = list(img.getdata())
    # create a string
    string = ''
    # for each pixel in the image
    count = 0
    while count != len(sequence):
        for pixel in pixels:
            if count == len(sequence):
                break
            if sequence[count] == 1:
                # get the red value of the pixel
                red = pixel[0]
                # get the character from the ascii value
                character = chr(red)
                # add the character to the string
                string += character
                count += 1
            elif sequence[count] == 2:
                # get the green value of the pixel
                green = pixel[1]
                # get the character from the ascii value
                character = chr(green)
                # add the character to the string
                string += character
                count += 1
            elif sequence[count] == 3:
                # get the blue value of the pixel
                blue = pixel[2]
                # get the character from the ascii value
                character = chr(blue)
                # add the character to the string
                string += character
                count += 1
    string = string.split('ÿ')
    return string[1]


def generate_seed(length):
    # create a list of 1 2 3
    list_of_123 = [1, 2, 3]
    # create a list to hold the random list
    random_list = []
    # for each number in the list
    for i in range(length):
        # add a random number from the list to the random list
        random_list.append(list_of_123[random.randint(0, 2)])
    # return the random list
    return random_list


# generates and returns two random numbers between 1 and 254
# these numbers are used to shift the rgb values of the pixels where the data is not
def generate_shifts():
    # generate the first random number
    shift1 = random.randint(1, 254)
    # generate the second random number
    shift2 = random.randint(1, 254)
    # return the two random numbers
    return shift1, shift2


# example of how to use the functions
# uncomment the lines below to see how the functions work
# -------------------------------------------- #

w = "This is a string of data that will be encrypted once and saved as img"

x = prism(w, 'data')  # encrypts the string and saves it as data.png and returns the seed
z = prism_decrypt("data.png", x)  # opens the image, takes in the seed as x, decrypts the image and returns the string
print(z)  # prints the string from the image

prism_hash("data.png", "img_hash")  # sorts the rgb values in the image with no index and saves it as img_hash.png
zz = compare_img_hash("data.png", "img_hash.png")  # compares the two images and returns True if they are the same
print(zz)  # prints True if the images are the same
