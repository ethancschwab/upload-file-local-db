from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys 

app = Flask(__name__)

db_file_path = os.path.abspath(os.getcwd()) + "/database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file_path


db = SQLAlchemy(app)

class Transaction(db.Model):
	transaction_id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer)
	product_id = db.Column(db.Integer)
	purchase_amount = db.Column(db.Integer)

class Customer(db.Model):
	customer_id = db.Column(db.Integer, primary_key=True)
	customer_firstname = db.Column(db.String(80), primary_key=True)

class Product(db.Model):
	product_id = db.Column(db.Integer, primary_key=True)
	product_name = db.Column(db.String(80))