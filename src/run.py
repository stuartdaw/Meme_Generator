from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

# print('started from run.py')
# print(Ingestor.parse('_data/DogQuotes/DogQuotesTXT.txt'))
meme = MemeEngine('_data/created_memes/test.jpg')

print(meme.make_meme('_data/photos/dog/xander_1.jpg',"When in doubt, go shoe-shopping", "jimbo"))

