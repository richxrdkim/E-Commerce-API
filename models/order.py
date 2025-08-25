# models/order.py
from extensions import db
from datetime import datetime
from .product import Product

# Association table
order_product = db.Table('order_product',
                         db.Column('order_id', db.Integer, db.ForeignKey(
                             'order.id'), primary_key=True),
                         db.Column('product_id', db.Integer, db.ForeignKey(
                             'product.id'), primary_key=True)
                         )


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    products = db.relationship('Product', secondary=order_product, lazy='subquery',
                               backref=db.backref('orders', lazy=True))
