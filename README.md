# upload-file-local-db
Upload .txt files to a SQLite local DB through a Python Flask Web App

Unfortunately ran out of time. Got the high level end to end logic working (file upload, file saving, text parsing, saving to Transaction table in database) but in the end I got caught up working out some devil in the details (converting datetime to string, generating UUID for transaction ID, logic for duplicate entries to the customer / product tables etc). If I had more time I would have liked to complete those details and soon after that add logic to cleanse the data, as well as expand the DB to include a User model for Authentication.

# Steps for Running
Prerequisites:
	Python3,
	SQLite - https://www.sqlite.org/download.html

Steps:

	1) Clone this repository

	2) Download pip and virtualenv
		python3 -m pip install --user upgrade pip ->
		python3 -m pip install --user virtualenv -> 
		python3 -m venv env 
	

	3) Activate virtualenv
		source env/bin/activate -> 
		pip install -r requirements.txt 
	

	4) Initialize DB
		python3 -> 
		from app import db -> 
		db.create_all()	
	

	5) Run App
		export FLASK_APP=app.py -> 
		flask run -> 
		enter http://localhost:5000/

	6) Data Validation (prints transaction objects)
		python3 ->
		from app import db, Transaction
		Transaction.query.all()

