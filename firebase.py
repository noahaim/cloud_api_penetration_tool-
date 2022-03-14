import firebase_admin
from firebase_admin import db
import json

# connect to Firebase
cred_obj = firebase_admin.credentials.Certificate('templates/finalproject-71cb6-firebase-adminsdk-1vkye-8bcdf57051.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': 'https://finalproject-71cb6-default-rtdb.firebaseio.com/'
	})

ref = db.reference("/")

with open("data.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)


