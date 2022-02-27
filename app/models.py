from app import db
from datetime import datetime as dt

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, default = dt.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)