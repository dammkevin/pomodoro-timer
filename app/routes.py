from flask import render_template, redirect, url_for, flash, request, jsonify
from app import db
from app.models import User
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

def home():
    return render_template('index.html')

def login():
    if request.method == 'POST':
        # Handle login logic here (placeholder)
        return redirect(url_for('home_route'))
    return render_template('login.html')

def register():
    if request.method == 'POST':
        # Handle registration logic here (placeholder)
        return redirect(url_for('login_route'))
    return render_template('register.html')

@login_required
def start_session():
    return jsonify({"message": "Pomodoro session started"})

@login_required
def end_session(session_id):
    return jsonify({"message": "Pomodoro session ended"})
