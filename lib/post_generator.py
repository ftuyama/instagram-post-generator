import os
import textwrap
from lib.utils import post_page, post_image
from PIL import Image, ImageDraw, ImageFont

TITLE_FONT = "assets/RobotoSerif-Bold.ttf"
TITLE_SIZE = 90
TITLE_COLOR = "#BA96F7"

TEXT_FONT = "assets/RobotoSerif-Regular.ttf"
TEXT_SIZE = 50
TEXT_COLOR = "#A780E7"
TEXT_OFFSET = 275

CAPTION_FONT = "assets/RobotoSerif-Bold.ttf"
CAPTION_SIZE = 72
CAPTION_COLOR = "#FFF"
CAPTION_STROKE = "#000"

POST_PICTURES = [
    'assets/begin.png',
    'assets/middle.png',
    'assets/end.png'
]

def get_template_image(image_filename):
    if os.path.exists(image_filename):
        return Image.open(image_filename)
    else:
        return Image.new('RGB', (1080, 1080), color='black')


def draw_title(image, draw, text):
    # Define the font and text to be added
    font = ImageFont.truetype(TITLE_FONT, TITLE_SIZE)

    # Get the size of the text
    text_width, text_height = draw.textsize(text, font)

    # Calculate the position of the text
    x = (image.width - text_width) / 2
    y = text_height / 2

    # Add the text to the image
    draw.text((x, y), text, font=font, fill=TITLE_COLOR)


def draw_sub_title(image, draw, text):
    # Define the font and text to be added
    font = ImageFont.truetype(TEXT_FONT, TEXT_SIZE)

    # Get the size of the text
    text_width, text_height = draw.textsize(text, font)

    # Calculate the position of the text
    x = (image.width - text_width) / 2
    y = TITLE_SIZE + 30 + text_height / 2

    # Add the text to the image
    draw.text((x, y), text, font=font, fill=TEXT_COLOR)


def draw_text(image, draw, text, offset):
    font = ImageFont.truetype(TEXT_FONT, TEXT_SIZE)

    image_width, image_height = image.size
    lines = textwrap.wrap(text, width=24)

    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text((200, offset), line, font=font, fill=TEXT_COLOR)
        offset += line_height + 12

def draw_caption_text(image, draw, text):
    font = ImageFont.truetype(CAPTION_FONT, CAPTION_SIZE)

    image_width, image_height = image.size
    lines = textwrap.wrap(text, width=24)
    total_size = sum(font.getsize(line)[1] for line in lines)
    offset = 1000 - total_size - CAPTION_SIZE

    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text((20, offset), line, font=font, fill=CAPTION_COLOR, stroke_width=10, stroke_fill=CAPTION_STROKE)
        offset += line_height + 12

def generate_post(post_title, post_subtitle, text):
    for index, picture in enumerate(POST_PICTURES):
        # Load the image
        image = get_template_image(picture)

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        draw_title(image, draw, post_title)
        draw_sub_title(image, draw, post_subtitle)

        if "middle" in picture:
            draw_text(image, draw, text, TEXT_OFFSET)

        # Save the modified image
        image.save(post_page(index + 1))


def generate_image_post(text):
    # Load the image
    image = Image.open(post_image())

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    draw_caption_text(image, draw, text)

    # Save the modified image
    image.save(post_image(final=True))
