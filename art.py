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

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)

    pixels = map_pixels_to_ascii(image)
    len_pixels = len(pixels)
    ascii_str = ""

    for i in range(0, len_pixels, new_width):
        ascii_str += pixels[i:i + new_width] + "\n"

    return ascii_str

if __name__ == "__main__":
    image_path = "path/to/your/image.png"  # Replace with the path to your PNG file
    output_width = 100  # Adjust the width as needed

    ascii_art = convert_image_to_ascii(image_path, output_width)
    print(ascii_art)
