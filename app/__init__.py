from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pomodoro.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app instance
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Import models after initializing extensions to avoid circular imports
    from app.models import User

    # Define user_loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import routes after app and extensions have been initialized
    from app.routes import home, login, register, start_session, end_session

    @app.route('/')
    def home_route():
        return home()

    @app.route('/login', methods=['GET', 'POST'])
    def login_route():
        return login()

    @app.route('/register', methods=['GET', 'POST']) 
    def register_route():
        return register()

    @app.route('/start_session', methods=['POST'])
    @login_required
    def start_session_route():
        return start_session()

    @app.route('/end_session/<int:session_id>', methods=['POST'])
    @login_required
    def end_session_route(session_id):
        return end_session(session_id)

    return app
