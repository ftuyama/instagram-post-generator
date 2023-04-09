import os
import sys
from lib.content import generate_content, guess_title
from lib.instagram import publish
from lib.image_generator import generate_image
from lib.post_generator import generate_post, generate_image_post

arguments = sys.argv

if len(arguments) < 2:
    params = ""
elif len(arguments) == 2:
    params = arguments[1]
else:
    params = arguments[1:]


def generate_post_content():
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

    return [post_title, post_subtitle, post_text]

if __name__ == '__main__':
    if params == "publish":
        print("Publishing post on Instagram")
        publish()
    elif params == "image":
        [post_title, post_subtitle, post_text] = generate_post_content()

        print("Generating image for post")
        generate_image(f"Cosmic spiritual {post_title} {post_subtitle}")

        print("Generating Instagram post")
        generate_image_post(post_text)
    else:
        [post_title, post_subtitle, post_text] = generate_post_content()

        print("Generating Instagram post")
        generate_post(post_title, post_subtitle, post_text)
