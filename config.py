import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Uggi1211!!@localhost/ecommerce_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey")
