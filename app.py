from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import os, sys, re, uuid
from datetime import datetime


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
	purchase_status = db.Column(db.String(8))
	purchase_amount = db.Column(db.Integer)
	# date_time = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return 'Transaction id %r ' %self.id

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(25))
	street_address = db.Column(db.String(40))
	state= db.Column(db.String(15))
	zip_code = db.Column(db.String(12))

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
	return file.filename + " uploaded successfully "


@app.route('/readfile')
def save_file_to_db(filename):
	path = current_path + "/files/" + filename
	file = open(path, 'r')
	lines = file.readlines()
	for line in lines:
		split = line.split("\t")
		customer_id=split[0]
		customer_first_name=split[1]
		customer_last_name=split[2]
		customer_street_address=split[3]
		customer_state=split[4]
		customer_zip=split[5]
		purchase_status=split[6]
		product_id=split[7]
		product_name=split[8]
		purchase_amount=split[9]
		# date_time=datetime.strptime(split[10], '%Y-%m-%d %H:%M:%S.%f')
		# date_time=datetime.fromisoformat(split[10])	

		transaction = Transaction(id=random.randint(1,200000), customer_id=customer_id, product_id=product_id, purchase_status=purchase_status,purchase_amount=purchase_amount)
		customer = Customer(id=customer_id, first_name=customer_first_name, last_name=customer_last_name,street_address=customer_street_address, state=customer_state, zip_code=customer_zip)
		product = Product(id=product_id, name=product_name)

		db.session.add(transaction)
		db.session.add(customer)
		db.session.add(product)
		db.session.commit()
	return "True"





@app.route('/data')
def display_data():
	return str(Transaction.query.first())