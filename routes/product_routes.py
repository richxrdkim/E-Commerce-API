# routes/product_routes.py
from flask import Blueprint, request, jsonify
from extensions import db
from models.product import Product
from schemas.product_schema import product_schema, products_schema

product_bp = Blueprint('products', __name__, url_prefix='/products')


@product_bp.route('', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)


@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)


@product_bp.route('', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        product_name=data['product_name'],
        price=data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)


@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    product.product_name = data.get('product_name', product.product_name)
    product.price = data.get('price', product.price)
    db.session.commit()
    return product_schema.jsonify(product)


@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"})
