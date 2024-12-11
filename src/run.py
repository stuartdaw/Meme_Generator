from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
import os

# print('started from run.py')
# print(Ingestor.parse('_data/DogQuotes/DogQuotesTXT.txt'))
meme = MemeEngine('_data/created_memes/test.jpg')

print(meme.make_meme('_data/photos/dog/xander_1.jpg',"When in doubt, go shoe-shopping", "jimbo"))


# Get the list of all files and directories
path = "_data/photos/dog"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)