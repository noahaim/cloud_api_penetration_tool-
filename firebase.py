import firebase_admin
from firebase_admin import db
import json

# connect to Firebase
cred_obj = firebase_admin.credentials.Certificate('templates/finalproject-71cb6-firebase-adminsdk-1vkye-8bcdf57051.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': 'https://finalproject-71cb6-default-rtdb.firebaseio.com/'
	})

ref = db.reference("/Users")
user=ref.child('user1')
user.set({
	'email': 'noa1998@gmail.com',
	'apiList':''
})
ref = db.reference("/Users/user1/apiList")
api=ref.child('api1')
api.set({
	'testList': ''
})
ref = db.reference("/Users/user1/apiList/api1/testList")
test=ref.child('test1')
test.set({
	'date': '12/12',
	'time': '14:00',
	'testResult': ''
})
ref = db.reference("/Users/user1/apiList/api1/testList/test1/testResult")
with open("data.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)



