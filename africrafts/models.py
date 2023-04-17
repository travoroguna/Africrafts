from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from flask_migrate import Migrate
import datetime


db = current_app.extensions["sqlalchemy"]

def now():
    return datetime.datetime.now(datetime.timezone.utc)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(255))


    def __str__(self) -> str:
        return f"User(username={self.username})"
    

class Artisan(db.Model):
    __tablename__ = 'artisans'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    shop_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(128))

    city = db.Column(db.String(128))
    country = db.Column(db.String(128))
    address = db.Column(db.String(128))



    def __str__(self) -> str:
        return f"Artisan(name={self.name})"