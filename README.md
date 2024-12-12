# Overview

Create a Meme generator whic matches images and quotes either by random or by user input. The quote is randomly placed on the image. The Meme Generator can be run on the command line or via flask.

![test](https://github.com/user-attachments/assets/3023935d-dbcb-4032-8082-4d6bbe782fc2)

# Instructions to run

#### CLI

The program can be run by using python3 app.py

If no parameters are added then the file and quote will be chosen at random from the existing quotes and pictures.

It has the following options:

meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

options:
  --path PATH      path to an image file
  --body BODY      quote body to add to the image
  --author AUTHOR  quote author to add to the image


#### FLASK

To run the application on a browser via flask, use the following code

export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload

Then the following code runs and you can click on the browser link after the "Running on" text.

 * Serving Flask app 'app.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3000


The user interface allows you to generate a random image or add your own image, quote and author via the form.


# Modular design


#### src module

Contains all modules and also the main app.py and meme.py python files to run the meme generator

#### QuoteEngine

The program reads all the quotes from csv, txt, pdf or word files. The document reader uses encapsulation to select the 
correct file reader to use based on the file extension. It is designed in modules which will further file type classes 
to be added or modified without major recoding. 

The QuoteEngine Module contains all the different ingestor's which have implement the base abstract IngestorInterface.

#### MemeEngine

This module contains the MemeEngine class which brings together the image and quote to create a meme.