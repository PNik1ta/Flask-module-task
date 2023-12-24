from dotenv import load_dotenv
import os
load_dotenv()

#controllers
from app.controllers.advice_controller import advice_bp
from app.controllers.challenge_controller import challenge_bp
from app.controllers.icebreaker_controller import icebreadker_bp
from app.controllers.topic_controller import topic_bp
from app.controllers.user_controller import user_bp

from app import create_app
app=create_app.create_app()

app.register_blueprint(advice_bp, url_prefix='/api')
app.register_blueprint(challenge_bp, url_prefix='/api')
app.register_blueprint(icebreadker_bp, url_prefix='/api')
app.register_blueprint(topic_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('FLASK_PORT')))