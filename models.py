from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    reminders = db.relationship('Reminder', backref='user', cascade="all, delete-orphan")

class Reminder(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    contest_id   = db.Column(db.Integer, nullable=False)
    contest_name = db.Column(db.String(200), nullable=False)
    remind_at    = db.Column(db.DateTime, nullable=False)
    sent         = db.Column(db.Boolean, default=False)
    user_id      = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)