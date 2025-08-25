# routes/__init__.py
from flask import Blueprint
from .user_routes import user_bp
from .product_routes import product_bp
from .order_routes import order_bp


def register_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
