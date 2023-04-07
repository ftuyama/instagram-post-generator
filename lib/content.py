import requests
from bs4 import BeautifulSoup
import random
import re

URL = "https://www.brainyquote.com/topics/spiritual-quotes"

def generate_content():
    # Make a request to the website and get the HTML content
    response = requests.get(URL)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the quote elements on the page
    quote_elements = soup.find_all("a", title="view quote")

    # Get a random quote element
    random_quote_element = random.choice(quote_elements)

    # Get the text of the quote
    quote_text = random_quote_element.text.strip()

    # Print the quote
    return quote_text

def guess_title(text):
    # Find all words in the text that have 4 or more characters
    words = re.findall(r'\b\w{5,}\b', text)

    # Pick a random word from the list of words
    random_word = random.choice(words)

    return random_word
