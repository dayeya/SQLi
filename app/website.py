from flask import Flask
from .views import views

DB_NAME = 'data/users.db'

def create_app() -> Flask:
    """
    Creates a simple Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')
    
    return app