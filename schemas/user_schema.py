# schemas/user_schema.py
from extensions import ma
from models.user import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)
