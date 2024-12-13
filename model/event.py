from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False)

    def get_event_date(self):
        return '-'.join(self.category[:10].split('-')[::-1])

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': self.get_event_date(),
        }