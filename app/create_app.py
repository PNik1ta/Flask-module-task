from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo
import os

def create_app():
	app = Flask(__name__)
	app.config['MONGO_URI'] = 'mongodb://' + os.environ.get('MONGO_HOST') + ':' + os.environ.get('MONGO_PORT') + '/' + os.environ.get('MONGO_DB')
	mongo = PyMongo(app)
	app.mongo = mongo
	return app