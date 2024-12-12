import textwrap
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    """ Class to create a meme from an image and a quote"""

    def __init__(self, out_path):
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500, keep=False) -> str:
        """ Method to generate a meme image

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the text to be displayed in the meme image.
            author {str} -- the author name to be displayed in the meme image.
            width {int} -- The pixel width value. Default=500.
            keep {bool} -- whether to keep the original image
        Returns:
            str -- the file path to the output image.
        """

        img = Image.open(img_path)

        if width > 500:
            width = 500

        ratio = width / float(img.size[0])
        height = int(ratio * img.size[1])
        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font_size = 20
        font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf',
                                  size=font_size)

        phrase = f'{text} - {author}'
        phrase_wrap = textwrap.wrap(phrase, width=35)

        # Check quote will fit on image
        if len(phrase_wrap) > (width / font_size):
            raise Exception("Quote is too long")

        max_width = 0
        total_height = 2
        line_heights = []

        for phrase in phrase_wrap:
            width = draw.textlength(phrase, font=font)
            max_width = max(max_width, width) + 2
            total_height += font_size
            line_heights.append(font_size)

        x = (img.width - max_width)
        y = (img.height - total_height)

        """ create a random image offset - check it will stay on image
        - a cant be more than x
        - b cant be more than y
        """
        x = x - random.randint(0, int(x))
        y = y - random.randint(0, int(y))

        # This puts the quote centrally aligned with its separate parts
        line_y = y
        for i in range(len(phrase_wrap)):
            line_x = x + (max_width - draw.textlength(phrase_wrap[i],
                                                      font=font)) // 2
            draw.text((line_x, line_y), phrase_wrap[i], font=font)
            line_y += line_heights[i]

        # To keep my computer clean but can choose to keep
        if keep:
            file = f'{self.out_path}/{random.randint(0, 1000000000)}.png'
        else:
            file = f'{self.out_path}/meme.jpg'

        img.save(file)

        return file
