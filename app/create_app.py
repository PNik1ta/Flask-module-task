from flask import Flask
from flask_pymongo import PyMongo
import os

#repositories
from repositories import AdviceRepository

#services
from services import AdviceService

def create_app():
	app = Flask(__name__)
	app.config['MONGO_URI'] = 'mongodb://' + os.environ.get('MONGO_HOST') + ':' + os.environ.get('MONGO_PORT') + '/' + os.environ.get('MONGO_DB')
	mongo = PyMongo(app)
	app.mongo = mongo

	#repositories
	adviceRepository = AdviceRepository(app)

	#services
	adviceService = AdviceService(adviceRepository)

	app.adviceService = adviceService
	return app