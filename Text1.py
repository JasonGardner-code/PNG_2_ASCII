from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=200):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def convert_text_to_ascii(text):
    ascii_str = ""
    for line in text.split('\n'):
        for char in line:
            ascii_str += char + " "
        ascii_str += "\n"
    return ascii_str

if __name__ == "__main__":
    input_text = "HELLO WORLD"
    
    ascii_str = convert_text_to_ascii(input_text)
    print(ascii_str)
