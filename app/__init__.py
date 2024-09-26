from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize SQLAlchemy, Bcrypt, and LoginManager (extensions)
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'  # Route name to redirect to when login is required
login_manager.login_message_category = 'info'  # Flash message category when login is required

def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Load configuration (either from a config file or hardcoded here)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pomodoro.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Import the routes
    from app import routes
    app.register_blueprint(routes.bp)  # If you're using blueprints, otherwise just import the routes

    return app
