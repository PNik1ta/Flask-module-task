from dotenv import load_dotenv
import os
load_dotenv()

#controllers
from app.controllers.advice_controller import advice_bp

from app import create_app
app=create_app.create_app()

app.register_blueprint(advice_bp, url_prefix='/api')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('FLASK_PORT')))