"""Python File to load and run the Meme Generator via Flask."""

import random
from flask import Flask, render_template, request
import os
import requests
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quote_lists = []
    for quote_file in quote_files:
        quote_lists.append(Ingestor.parse(quote_file))

    if len(quote_lists) == 0:
        raise Exception('No quotes found')

    quotes = []
    for q_list in quote_lists:
        for q in q_list:
            quotes.append(q)

    imgs = []
    dir_list = os.listdir('_data/photos/dog')

    for file in dir_list:
        if file.endswith(".jpg") or file.endswith(".png"):
            imgs.append(file)

    if len(imgs) == 0:
        raise Exception('No images found')

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    img = f'_data/photos/dog/{img}'
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.quote, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    url = request.form.get('image_url')
    print(url)
    web_quote = request.form.get('body')
    web_author = request.form.get('author')
    tmp = f'./static/{random.randint(0, 1000000000)}.png'

    web_image = requests.get(url).content
    with open(tmp, 'wb') as img:
        img.write(web_image)

    try:
        path = meme.make_meme(tmp, web_quote, web_author)
    except Exception as e:
        path = f'./static/nd_valid_url.png'

    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    try:
        app.run()
    except Exception as e:
        print(e)
