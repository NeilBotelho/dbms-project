from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY']='POpZbta8mpk2CaflKWlfDA'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
bcrypt=Bcrypt(app)
db=SQLAlchemy(app)

# print(bcrypt)

from sailor import routes