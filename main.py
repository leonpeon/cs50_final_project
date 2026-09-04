# TODO ASCII ART GENERATOR
# First: Turn images into ASCII ART
# Second: Randomly generate faces.
# Third: Create town?

from PIL import Image
import shutil

# Gradient of values for ASCII art
VALUES = " .`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
VALUES_2 = " .:-=+*#%@"

# Gives image object
img = Image.open("test_img.jpg")

face_img = Image.open("face_img.jpg")

# Thumbnail
size = (100, 100)
face_img.thumbnail(size)
face_img.save('face_img.jpg')

new_width = 100
new_height = int(img.height / img.width * new_width * 0.8)
face_img = face_img.resize((new_width, new_height))

# TODO Loop through each pixel and turn it into a character
width, height = face_img.size

for y in range(height):
    for x in range(width):
        # Calculates the brightness of the pixel, then ascribes it the corresponding ASCII char
        red, green, blue = face_img.getpixel((x,y))
        brightness = round(0.299*red + 0.587*green +0.114*blue)

        with open("ascii.txt", "a") as file:
            if brightness < 255/len(VALUES_2):
                file.write(VALUES_2[0])
            else:
                file.write(VALUES_2[brightness // round(255/len(VALUES_2))])

            if x == width - 1:
                file.write("\n")
