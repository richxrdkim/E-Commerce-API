# schemas/product_schema.py
from extensions import ma
from models.product import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = True


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
