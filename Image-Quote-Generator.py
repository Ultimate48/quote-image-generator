import textwrap
from random import randint
import fetchQuote
from PIL import Image, ImageDraw, ImageFont


def generateImageQuote():
    quote = fetchQuote.fetchQuote()
    random = randint(1, 9)
    image = "Images/" + "00000" + str(random) + ".jpg"
    return quote, image


def create_image_with_text(image_path, text):
    # Load the image
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Choose a font and size
    # font_path = "path/to/your/font.ttf"  # You can specify a TrueType font file (ttf)
    font_size = 50
    font = ImageFont.truetype("font.ttf", font_size)

    # Choose text color
    text_color = (255, 255, 255)  # RGB values for white

    # Choose position to paste the text
    text_position = (50, 50)

    wrapped_text = textwrap.fill(text, width=image.width)

    # Paste the text onto the image
    draw.text(text_position, wrapped_text, font=font, fill=text_color)

    # Save the modified image as output.jpg
    output_path = "output.jpg"
    image.save(output_path)


create_image_with_text(generateImageQuote()[1], generateImageQuote()[0])
