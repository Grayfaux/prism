# prism
prism is a tool that encrypts data into an image, you can also  hash to an image and compare the image to the hash image similar to password hashing

Pillow is required for img processing (pip install Pillow)

prism(string: str, new_name: str)
takes a string of data and encrypts it into an image, saves the image,
and returns the seed of where the data is in the rgb spectrum of the image. the seed is needed to decrypt the image.

prism_decrypt(image, sequence)
takes an image and returns a string of the characters in the image based on the sequence seed.

generate_seed(length)
creates a seed or list of 1, 2 and 3 in random order for a given length. already in use inside the prism function.

generate_shifts()
generates and returns two random numbers between 1 and 254.
these numbers are used to shift the rgb values of the pixels where the data is not.
already in use inside the prism function.

prism_decrypt(image, sequence)
takes an image and returns a string of the characters in the image based on the sequence seed.

prism_hash(image, new_name)
takes an image and rearranges the pixels in ascending order from top to bottom and saves it as a new image with the name passed in the new_name argument.

compare_img_hash(image, hash_image)
takes two images and counts the number of times each color appears in both images and if they are the same return true else return false.

an example use can be found at the bottom of the python file. Just uncomment and run.


Notes:
Img generation
You may notice that the image appears to be random. This is because the seed and the color shifts are run inside the prism() function.
These are used to obscure the final image but will not affect to return of the data as long as the correct seed is passed into prism_decrypt(image, sequence).
prism() returns this seed as a list of the sequence that was generated internally, without this you can not decrypt the img.

Img hash
prism_hash(image, new_name) works by sorting the rgb values from top to bottom from 0 at the top to 255 at the bottom.
no index is returned, nor the location of the data inside the rgb spectrum.
This means prism can be used exclusively for hashing, encryption or a combo of hash and encryption.
