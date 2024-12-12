import os
import random
import argparse

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path
        # img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    # meme = MemeEngine('./tmp')
    meme = MemeEngine('_data/created_memes/')

    path = meme.make_meme(img, quote.quote, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description='Generate a meme')
    parser.add_argument('--path', type=str)
    parser.add_argument('--body', type=str)
    parser.add_argument('--author', type=str)
    args = parser.parse_args()

    print(f"path: {args.path}")

    print(generate_meme(args.path, args.body, args.author))
