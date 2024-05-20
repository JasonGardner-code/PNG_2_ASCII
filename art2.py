from PIL import Image

def convert_to_ascii(filepath, token_count='medium'):
    img = Image.open(filepath).convert('L')  # Convert image to grayscale
    width, height = img.size

    # Adjust image size based on token count
    if token_count == 'low':
        img = img.resize((width // 2, height // 2))
    elif token_count == 'high':
        img = img.resize((width * 2, height * 2))

    ascii_chars = '@%#*+=-:. '
    pixels = img.getdata()
    ascii_str = ''.join([ascii_chars[pixel // 32] for pixel in pixels])
    ascii_art = '\n'.join([ascii_str[i:i + width] for i in range(0, len(ascii_str), width)])
    return ascii_art

# Ensure you have the PNG to ASCII conversion logic correctly implemented