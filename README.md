# instagram-post-generator

Generates posts for Instagram with spiritual quotes

## Setup

Create a .env file with this content:

```bash
INSTAGRAM_USERNAME='yourusername'
INSTAGRAM_PASSWORD='password'
```

Install project

```bash
git clone git@github.com:ftuyama/instagram-post-generator.git
make install
```

## How to use

Creating the Instagram Post:

```bash
make run
```

Publishing the post on Instagram:

```bash
make publish
```

## Advanced

You may also generate a post image based on the generated post content.

For that, setup your OPENAI token:

```bash
OPENAI_TOKEN="..."
```

Then run:

```bash
make image
```
