from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(150))
    code = db.Column(db.String(150))
    password = db.Column(db.String(150))