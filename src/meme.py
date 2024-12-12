"""Python file to create meme from the CLI."""
import os
import random
import argparse
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None) -> str:
    """Generate a meme given a path and a quote.

    Arguments:
    path {str} -- the file location for the input image.
    body {str} -- the text to be displayed in the meme image.
    author {str} -- the author name to be displayed in the meme image.

    Returns:
    str -- the file path to the output image.
    """
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

    meme = MemeEngine('_data/created_memes')

    path = meme.make_meme(img, quote.quote, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a meme')
    parser.add_argument('--path', type=str,
                        help='path to an image file')
    parser.add_argument('--body', type=str,
                        help='quote body to add to the image')
    parser.add_argument('--author', type=str,
                        help='quote author to add to the image')
    args = parser.parse_args()

    try:
        print(generate_meme(args.path, args.body, args.author))
    except Exception as e:
        print(e)