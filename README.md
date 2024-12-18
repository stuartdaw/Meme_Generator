# Overview

Create a Meme generator which matches images and quotes either by random or by user input. The quote is randomly placed on the image. The Meme Generator can be run on the command line or via flask.

The project uses libraries such as pillow, python-docx, pandas, flask, argparse and os.

![smaller_memes](https://github.com/user-attachments/assets/d95e1f3d-7ab9-4ab1-bab0-cc23907faed3)

# Instructions to run

#### CLI

The program can be run by using python3 app.py

If no parameters are added then the file and quote will be chosen at random from the existing quotes and pictures.

It has the following options:

meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

options:
  --path PATH      path to an image file eg. --path "_data/photos/dog/xander_2.jpg"
  --body BODY      quote body to add to the image
  --author AUTHOR  quote author to add to the image

If you enter a quote but not an author the program will stop.
If you enter an author but not a quote it will assign a random quote and author.

#### FLASK

To run the application on a browser via flask, use the following code

python3 app.py

Then the following code runs, and you can click on the browser link after the "Running on" text.

 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000


The user interface allows you to generate a random image or add your own image, quote and author via the form.


# Modular design


#### src module

Contains all modules and also the main app.py and meme.py python files to run the meme generator

#### QuoteEngine module

The program reads all the quotes from csv, txt, pdf or word files. The document reader uses encapsulation to select the 
correct file reader to use based on the file extension. It is designed in modules which will further file type classes 
to be added or modified without major recoding. 

The QuoteEngine Module contains all the different ingestor's which have implement the base abstract IngestorInterface.

#### MemeEngine module

This module contains the MemeEngine class which brings together the image and quote to create a meme.

# References

I used the following articles and code examples to help me to learn how to manipulate text onto an image. 
They allowed me to create a way to center the text in lines and also to prevent it from running off the image.

https://wellsr.com/python/centering-text-vertically-and-horizontally-using-pillow/
- how to wrap quotes and centre

https://github.com/python-pillow/Pillow/issues/6938
- to help centre image and prevent image going outside of bounds
