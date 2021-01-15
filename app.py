from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os, sys, re 


# Initialization 
app = Flask(__name__)
current_path = os.path.abspath(os.getcwd()) 
db_file_path = current_path + "/database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file_path
app.config['UPLOAD_FOLDER'] = current_path + "/files"
db = SQLAlchemy(app)



# Database Models
class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
	product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
	purchase_amount = db.Column(db.Integer)

	def __repr__(self):
		return 'Transaction id %r ' %self.id

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80), primary_key=True)

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))




#Web App Pages
@app.route('/')
def home():		
	return render_template('upload.html')



@app.route('/upload', methods=['POST'])
def receive_file():
	file = request.files['input-file']
	file.save(current_path + "/files/" + file.filename)
	save_file_to_db(file.filename)

	return file.filename


# Sample data insertion
@app.route('/insertDB')
def insert():
	transaction = Transaction(id=1234, customer_id=1, product_id=100, purchase_amount=321.2)
	customer = Customer(id=1, first_name='john')
	product = Product(id=100, name='toaster')
	db.session.add(transaction)
	db.session.add(customer)
	db.session.add(product)
	db.session.commit()

	return 'Data Insert Successful'

@app.route('/data')
def display_data():
	return str(Transaction.query.first())

@app.route('/readfile')
def save_file_to_db(filename):
	path = current_path + "/files/" + filename
	file = open(path, 'r')
	lines = file.readlines()
	for line in lines:
		split = line.split("\t")
		for term in split:
			app.logger.error(term)
	return "True"