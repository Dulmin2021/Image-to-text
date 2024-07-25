from PIL import Image
import numpy as np

# Define the ASCII characters
ASCII_CHARS = "@%#*+=-:. "

# Resize the image while maintaining aspect ratio
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert the image to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Map each pixel to an ASCII character based on intensity
def pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    for pixel_value in pixels:
        for pixel in pixel_value:
            ascii_str += ASCII_CHARS[pixel // 32]
        ascii_str += "\n"
    return ascii_str

# Convert the image to ASCII art
def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    image = resize_image(image, new_width)
    image = grayify(image)
    
    ascii_str = pixels_to_ascii(image)
    return ascii_str

# Save the ASCII art to a text file
def save_ascii_art(ascii_str, output_file):
    with open(output_file, "w") as f:
        f.write(ascii_str)

# Example usage
image_path = "path_to_your_image.jpg"
output_file = "ascii_image.txt"

ascii_art = image_to_ascii(image_path)
save_ascii_art(ascii_art, output_file)
print(ascii_art)
