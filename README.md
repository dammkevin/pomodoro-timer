# Pomodoro Timer Web Application

This project is a full-stack web application that implements a Pomodoro Timer to help users boost productivity through time-blocking techniques. It allows users to register, log in, and track Pomodoro sessions while securely storing data in a database.

## Introduction

This application provides a structured method to manage focus sessions and breaks using the Pomodoro technique. It features user authentication, session management, and database storage to keep track of users and their session history.

The timer supports starting, stopping, and resetting functionality with visual indicators, and all data is stored securely in SQLite using Flask-SQLAlchemy.

## Features

- **User Authentication**
  - Secure registration and login with hashed passwords.
  - Session management using Flask-Login.
- **Pomodoro Timer**
  - Timer start, stop, and reset options.
  - Tracks Pomodoro sessions with timestamps.
- **Database Integration**
  - Stores user and session data in SQLite.
  - Dynamic session tracking linked to individual users.
- **Responsive Design**
  - Mobile-friendly and works seamlessly across devices.
- **Flash Messages**
  - Provides real-time feedback for user actions.

## Technologies Used

- **Python 3.x**
- **Flask Framework**
  - Flask-SQLAlchemy - ORM for database handling.
  - Flask-Bcrypt - Secure password hashing.
  - Flask-Login - User session management.
  - Flask-WTF - Form handling and validation.
- **Frontend**
  - HTML/CSS for structure and styling.
  - JavaScript for dynamic timer functionality.
- **Database**
  - SQLite for lightweight and local data storage.
