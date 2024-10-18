from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import login_required


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pomodoro.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Import route functions
    from app.routes import home, login, start_session, end_session

    # Associate the routes with the `app` instance
    @app.route('/')
    def home_route():
        return home()

    @app.route('/login', methods=['GET', 'POST'])
    def login_route():
        return login()

    @app.route('/start_session', methods=['POST'])
    @login_required
    def start_session_route():
        return start_session()

    @app.route('/end_session/<int:session_id>', methods=['POST'])
    @login_required
    def end_session_route(session_id):
        return end_session(session_id)

    return app
