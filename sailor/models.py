from datetime import datetime
from sailor import db
from flask_table import Table, Col

# from flask


class Entry(db.Model):
    ID=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=False,nullable=False)
    rating=db.Column(db.Integer,primary_key=False,nullable=False)
    age=db.Column(db.Integer,primary_key=False,nullable=False)
    def __repre__(self):
        return f'Entry("{self.ID}",{self.name})'


