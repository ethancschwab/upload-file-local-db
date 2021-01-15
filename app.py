from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os, sys 


# Initialization 
app = Flask(__name__)
db_file_path = os.path.abspath(os.getcwd()) + "/database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file_path
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.getcwd()) + "/files"
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
	# open(file)
	file.save(os.path.join(os.getcwd()) + "/files/" + file.filename)
	# file.save(os.path.join(app.config['UPLOAD_FOLDER'])
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

	return 'Data Insert Successfully'

@app.route('/data')
def display_data():
	return str(Transaction.query.first())