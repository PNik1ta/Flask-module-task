from dotenv import load_dotenv
import os

load_dotenv()

from app import create_app

app=create_app.create_app()

if __name__ == '__main__':
	app.run(debug=True, port=int(os.environ.get('FLASK_PORT')))