# schemas/order_schema.py
from extensions import ma
from models.order import Order
from schemas.product_schema import ProductSchema


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True

    products = ma.Nested(ProductSchema, many=True)


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
