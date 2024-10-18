print("Starting models.py...")  # This should print when the file is loaded

from app import db
from flask_login import UserMixin
from datetime import datetime

print("Imports successful")  # This should print if imports succeed

class User(UserMixin, db.Model):
    print("Defining User class")
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Session(db.Model):
    print("Defining Session class")
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.String(20), nullable=False, default='ongoing')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Session('{self.id}', '{self.status}')"

print("models.py has been successfully loaded")  # This should print if everything works
