import requests
from bs4 import BeautifulSoup
import random
import requests
import re

BRAINY_QUOTE_URL = "https://www.brainyquote.com/topics/spiritual-quotes"
ZEN_QUOTES_URL = "https://zenquotes.io/api/random"

def brainy_quote():
    # Make a request to the website and get the HTML content
    response = requests.get(BRAINY_QUOTE_URL)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the quote elements on the page
    quote_elements = soup.find_all("a", title="view quote")

    # Get a random quote element
    random_quote_element = random.choice(quote_elements)

    # Get the text of the quote
    quote_text = random_quote_element.text.strip()

    return quote_text

def zen_quote():
    response = requests.get(ZEN_QUOTES_URL)

    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f'{quote} - {author}'
    else:
       return 'Error fetching quote'


def generate_content():
    quote_text = random.choice([brainy_quote, zen_quote])()

    if len(quote_text) > 120:
        quote_text = quote_text.split('.')[0]

    # Print the quote
    return quote_text

def guess_title(text):
    # Find all words in the text that have 4 or more characters
    words = re.findall(r'\b\w{5,}\b', text)

    # Pick a random word from the list of words
    random_word = random.choice(words)

    return random_word
