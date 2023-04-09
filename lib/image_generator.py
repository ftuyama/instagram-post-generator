import os
import openai
import urllib.request
from dotenv import load_dotenv
from lib.utils import post_image

load_dotenv()
openai.api_key = os.environ.get('OPENAI_TOKEN')

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, post_image())
