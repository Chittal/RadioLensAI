from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')

    from app.routes import main_routes
    app.register_blueprint(main_routes)

    return app