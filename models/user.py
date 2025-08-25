# models/user.py
from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True, nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)
