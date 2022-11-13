# prism
prism is a tool that encrypts data into an image, you can also  hash to an image and compare the image to the hash image similar to password hashing.

example images for encryption and the hash of that encryption have been included in project files.

Pillow is required for img processing (pip install Pillow)

prism(string: str, new_name: str)
takes a string of data and encrypts it into an image, saves the image,
and returns the seed of where the data is in the rgb spectrum of the image. the seed is needed to decrypt the image.

prism_decrypt(image, sequence)
takes an image and returns a string of the characters in the image based on the sequence seed.

generate_seed(length)
creates a seed or list of 1, 2 and 3 in random order for a given length. seed length must match the length of the input data.
i.e. sequence = generate_seed(len(input_data))
when encrypting, the seed is returned and MUST be used to decrypt the image. 
when hashing or comparing something like hashed passwords, the seed will need to be stored and used to compare the images.

generate_shifts()
generates and returns two random numbers between 1 and 254.
these numbers are used to shift the rgb values of the pixels where the data is not.

prism_decrypt(image, sequence)
takes an image and returns a string of the characters in the image based on the sequence seed.

prism_hash(image, new_name)
takes an image and rearranges the pixels in ascending order from top to bottom and saves it as a new image with the name passed in the new_name argument.

compare_img_hash(image, hash_image)
takes two images and counts the number of pixels and the number of times each color appears in both images and if they are the same return true else return false.

an example use can be found at the bottom of the python file. Just uncomment and run.


Notes:

Img hash
prism_hash(image, new_name) works by sorting the rgb values from top to bottom from 0 at the top to 255 at the bottom.
no index is returned, nor the location of the data inside the rgb spectrum.
This means prism can be used exclusively for hashing, encryption or a combo of hash and encryption.

when using prism for encryption only the seed will need to be stored for decryption.
when using prism for hashing both the seed and the shift values will need to be stored to compair new input to the original hash.
