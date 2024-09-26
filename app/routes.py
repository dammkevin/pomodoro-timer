from flask import render_template, request, jsonify, redirect, url_for
from app import app, db
from flask_login import login_required, current_user

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/start_session', methods=['POST'])
@login_required
def start_session():
    # Logic to start a Pomodoro session
    return jsonify({"message": "Pomodoro session started"})

@app.route('/end_session/<int:session_id>', methods=['POST'])
@login_required
def end_session(session_id):
    # Logic to end a Pomodoro session
    return jsonify({"message": "Pomodoro session ended"})
