import random
from flask import Flask, render_template, request
import os
import requests


# @TODO Import your Ingestor and MemeEngine classes
from .QuoteEngine import Ingestor, QuoteModel
from .MemeEngine import MemeEngine
app = Flask(__name__)

# meme = MemeEngine('./_data/created_memes')
meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    # print("do setup")
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quote_lists = []
    for quote_file in quote_files:
        quote_lists.append(Ingestor.parse(quote_file))

    quotes = []
    for q_list in quote_lists:
        for q in q_list:
            quotes.append(q)

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    dir_list = os.listdir('_data/photos/dog')

    for file in dir_list:
        if file.endswith(".jpg") or file.endswith(".png"):
            imgs.append(file)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    img = f'_data/photos/dog/{img}'
    quote = random.choice(quotes)
    print(f'img: {img}, q: {quote.quote}, a: {quote.author}')
    path = meme.make_meme(img, quote.quote, quote.author)
    print(f'path in meme_rand: {path}')

    return render_template('meme.html', path=path) #changed from path=path


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    print('in meme_post')
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    url = request.form.get('image_url')
    web_quote = request.form.get('body')
    web_author = request.form.get('author')

    web_meme_eng = MemeEngine('./static')

    tmp = f'./static/{random.randint(0, 1000000000)}.png'

    web_image = requests.get(url).content
    with open(tmp, 'wb') as img:
        img.write(web_image)

    path = web_meme_eng.make_meme(tmp, web_quote, web_author)

    os.remove(tmp)
    print(f'path to be sent to html: {path}')
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
