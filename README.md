# upload-file-local-db
Upload .txt files to a SQLite local DB through a Python Flask Web App


# Steps for Running
Prerequisites:
	Python3
	SQLite - https://www.sqlite.org/download.html

Steps:
	1) Download pip and virtualenv
		python3 -m pip install --user upgrade pip
		python3 -m pip install --user virtualenv
		python3 -m venv env 
	2) Activate virtualenv
		source env/bin/activate
		pip install -r requirements.txt 
	3) Initialize DB
		python3
		from app import db
		db.create_all()	
	4) Run App
		export FLASK_APP=app.py
		flask run
		enter http://localhost:5000/
