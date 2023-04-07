import os
import sys
from lib.content import generate_content, guess_title
from lib.instagram import publish
from lib.post_generator import generate_post

arguments = sys.argv

if len(arguments) < 2:
    params = ""
elif len(arguments) == 2:
    params = arguments[1]
else:
    params = arguments[1:]

if __name__ == '__main__':
    if params == "publish":
        print("Publishing post on Instagram")
        publish()
    else:
        if type(params) != list:
            print("Generating content for you!")

            post_text = generate_content()
            post_title = guess_title(post_text).upper()
            post_subtitle = guess_title(post_text).title()
        else:
            post_title = params[0].upper()
            post_subtitle = params[1].title()
            post_text = params[2]

        print(f"Title: {post_title}")
        print(f"Subtitle: {post_subtitle}")
        print(f"Text: {post_text}")

        print("Generating Instagram post")
        generate_post(post_title, post_subtitle, post_text)

