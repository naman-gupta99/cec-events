from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EventRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    event_id = db.Column(db.String(80), nullable=False)