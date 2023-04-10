# instagram-post-generator

Generates posts for Instagram with spiritual quotes

## Setup

Create a .env file with this content:

```bash
INSTAGRAM_USERNAME='yourusername'
INSTAGRAM_PASSWORD='password'
OPENAI_TOKEN="..." # Optional, for image generation
IMAGE_FLAVOUR="Cosmic spiritual" # Optional, param used to generate OpenAI image
```

Install project

```bash
git clone git@github.com:ftuyama/instagram-post-generator.git
make install
```

## How to use

Creating the Instagram Post (it will generate an image with OpenAI + fetch a random quote from internet):

```bash
make run
```

Publishing the post on Instagram:

```bash
make publish
```

## Example

![Example image](example.png "Example of AI generated post")

## Advanced

You may also generate a post using a pre-defined template.

```bash
make template
```

For that, you need to setup in `assets/` folder three images: `begin.png`, `middle.png` and `end.png`
