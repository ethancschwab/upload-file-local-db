from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os, sys 

app = Flask(__name__)

db_file_path = os.path.abspath(os.getcwd()) + "/database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file_path


db = SQLAlchemy(app)

class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
	product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
	purchase_amount = db.Column(db.Integer)


class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80), primary_key=True)

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))


@app.route('/')
def home():		
	return render_template('upload.html')

@app.route('/upload')
def receive_file():
	file = request.files['input-file']
	app.logger.error(file.filename)
	return file.filename

@app.route('/insertDB')
def insert():
	transaction = Transaction(id=1234, customer_id=1, product_id=100, purchase_amount=321.2)
	customer = Customer(id=1, first_name='john')
	product = Product(id=100, name='toaster')
	db.session.add(transaction)
	db.session.add(customer)
	db.session.add(product)
	db.session.commit()

	return 'it worked'