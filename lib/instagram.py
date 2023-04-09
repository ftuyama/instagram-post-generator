import os
import io
from PIL import Image
from lib.utils import post_page
from instagram_private_api import Client, ClientCompatPatch
from dotenv import load_dotenv

load_dotenv()
username = os.environ.get('INSTAGRAM_USERNAME')
password = os.environ.get('INSTAGRAM_PASSWORD')

def prepare_image(image_index):
    image = Image.open(post_page(image_index))

    data = io.BytesIO()
    image.save(data, 'png')

    return data.getvalue()

def publish():
    api = Client(username, password)

    # Define the photo path and caption
    medias = [
        {"type": "image", "size": (1080, 1080), "data": prepare_image(1) },
        {"type": "image", "size": (1080, 1080), "data": prepare_image(2) },
        {"type": "image", "size": (1080, 1080), "data": prepare_image(3) }
    ]

    # Define post caption
    caption = "#spirituality #awakenedcat #spiritual #spiritualawakening #enlightenment #meditation #mindfulness #consciousness #higherconsciousness #awakening #selflove #peace #love #innerpeace #gratitude #healing #soul #universalconsciousness #mindbodysoul #mindbodyspirit #chakras #energyhealing #positivevibes #positivity #wisdom #transformation #universe #oneness"

    # Upload the photo
    api.post_album(medias, caption=caption)


