from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'app/database.db'
    app.register_blueprint(main)
    return app