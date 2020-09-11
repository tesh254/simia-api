from app import db
from sqlalchemy.dialects.postgresql import JSON


class Developer(db.Model):
    __tablename__ = "developer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)
