Overview

Create a Meme generator whic matches images and quotes either by random or by user input. The quote is randomly placed on the image. The Meme Generator can be run on the command line or via flask.

![test](https://github.com/user-attachments/assets/3023935d-dbcb-4032-8082-4d6bbe782fc2)

Instructions to run

CLI


FLASK

export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload


Modular design

The program reads all the quotes from csv, txt, pdf or word files. The document reader uses encapsulation to select the correct file reader to use based on the file extension. 
It is designed in modules which will further file type classes to be added or modified without major recoding. 
