from flask import render_template, request, jsonify, redirect, url_for, flash
from app import db, bcrypt
from app.models import User, Session
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# User Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    # If the user is already logged in, redirect to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

# User Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is already logged in, redirect to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    
    return render_template('login.html', form=form)

# User Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Route to start a Pomodoro session
@app.route('/start_session', methods=['POST'])
@login_required
def start_session():
    session = Session(user_id=current_user.id, start_time=datetime.utcnow(), status='ongoing')
    db.session.add(session)
    db.session.commit()
    return jsonify({"message": "Pomodoro session started", "session_id": session.id})

# Route to end a Pomodoro session
@app.route('/end_session/<int:session_id>', methods=['POST'])
@login_required
def end_session(session_id):
    session = Session.query.get_or_404(session_id)
    
    # Ensure that the session belongs to the current user
    if session.user_id != current_user.id:
        return jsonify({"message": "You are not authorized to end this session."}), 403
    
    session.end_time = datetime.utcnow()
    session.status = 'completed'
    db.session.commit()
    
    return jsonify({"message": "Pomodoro session ended"})
