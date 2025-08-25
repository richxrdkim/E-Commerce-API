# routes/order_routes.py
from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order
from models.product import Product
from schemas.order_schema import order_schema, orders_schema
from datetime import datetime

order_bp = Blueprint('orders', __name__, url_prefix='/orders')


@order_bp.route('', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(
        user_id=data['user_id'],
        order_date=datetime.strptime(
            data.get('order_date', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S')
    )
    db.session.add(new_order)
    db.session.commit()
    return order_schema.jsonify(new_order)


@order_bp.route('/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    if product not in order.products:
        order.products.append(product)
        db.session.commit()
    return order_schema.jsonify(order)


@order_bp.route('/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    if product in order.products:
        order.products.remove(product)
        db.session.commit()
    return order_schema.jsonify(order)


@order_bp.route('/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return orders_schema.jsonify(orders)


@order_bp.route('/<int:order_id>/products', methods=['GET'])
def get_products_in_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify([{"id": p.id, "product_name": p.product_name, "price": p.price} for p in order.products])


@order_bp.route('', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return orders_schema.jsonify(orders)
