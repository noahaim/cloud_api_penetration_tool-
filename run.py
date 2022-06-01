"""
Main program run file
"""
import json
from getpass import getpass
import firebase_admin
from firebase_admin import db
from firebase_admin import auth

from flask import Flask, render_template, url_for, request, session
import requests
from werkzeug.utils import redirect

from flask import Flask, render_template, redirect, request, session
from flask_session import Session
import testBRTFRC
import testDOS
import testJSONJCTN
import testXSS
from API import API
from run_class import Run
from test_resaults import TestRes
import pyrebase
import datetime

from user import user

app = Flask(__name__)
config = {
    "apiKey": "AIzaSyCNmdtg0fjdCXoXXkUSxqSiIYuzl_50R4Y",
    "authDomain": "finalproject-71cb6.firebaseapp.com",
    "projectId": "finalproject-71cb6",
    "databaseURL": "https://finalproject-71cb6-default-rtdb.firebaseio.com/",
    "storageBucket": "finalproject-71cb6.appspot.com",
    "messagingSenderId": "463492559459",
    "appId": "1:463492559459:web:8f42ae5c51143311703e56",
    "measurementId": "G-DKJWRJQHP1"
}
cred_obj = firebase_admin.credentials.Certificate('templates/finalproject-71cb6-firebase-adminsdk-1vkye-8bcdf57051.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': 'https://finalproject-71cb6-default-rtdb.firebaseio.com/'
	})


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
# db=firebase.database()

@app.route('/dashboard')
@app.route('/')
def dashboard():
    data = {}

    brt1 = TestRes("Bruteforce simple", testBRTFRC.simple_brtfrc(), "got into system").writeToJson()
    brt2 = TestRes("Bruteforce dictionary", testBRTFRC.rand(), "passed dictionary").writeToJson()
    brt3 = TestRes("Bruteforce random", testBRTFRC.dict(), "Did not block").writeToJson()

    brt_list = [brt1, brt2, brt3]
    data["Authentication Bruteforce"] = brt_list

    dos1 = TestRes("DoS simple", testDOS.testDOS(), "did not block").writeToJson()
    dos2 = TestRes("Dos spoofed ip", testDOS.testDOS(spoofIP=True), "did not block").writeToJson()
    dos3 = TestRes("DoS random queries", testDOS.testDOS(randomQueries=True), "did not block").writeToJson()
    dos4 = TestRes("DoS spoofed ip + random", testDOS.testDOS(spoofIP=True, randomQueries=True),
                   "did not block").writeToJson()

    dos_list = [dos1, dos2, dos3, dos4]
    data["Denial Of Service"] = dos_list

    xss1 = TestRes("Simple redirects", testXSS.simple_redirect(), "redirected!").writeToJson()
    xss2 = TestRes("Write data", testXSS.write_data(), "changed page data").writeToJson()
    xss3 = TestRes("Delete data", testXSS.delete_data(), "data was deleted from page").writeToJson()

    xss_list = [xss1, xss2, xss3]
    data["Cross Site Scripting"] = xss_list

    inj1 = TestRes("Simple string", testJSONJCTN.simple_string(), "was not detected").writeToJson()
    inj2 = TestRes("Get data", testJSONJCTN.insert_data(), "returned data").writeToJson()
    inj3 = TestRes("Insert data", testJSONJCTN.get_pass(), "file was changed").writeToJson()

    inj_list = [inj1, inj2, inj3]
    data["JSON injection"] = inj_list

    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    image_file_vi = url_for('static', filename='images/v1.jpeg')
    image_file_x = url_for('static',filename='images/x2.jpeg')
    return render_template(
        'dashboard.html', image_file_vi=image_file_vi,image_file_x=image_file_x,
        data=data
    )
userID=""
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            u=auth.sign_in_with_email_and_password(email, password)
            userID=db.reference("/Users").child(u['localId'])
            # print(ref.get()['name'])
            # return auth.get_account_info(u['idToken'])
            return allAPI(userID)
        except:
            return render_template('login.html', us='Please check your credentials')

    return render_template('login.html')

#שליפה של כל הAPI של המשתמש הספציפי והעברה של המידע לHTML
@app.route('/allAPI')
def allAPI(userID):
    # s = requests.Session()
    # s['id']=userID
    # session["id"] = userID
    # print(userID.key)
    return render_template("allAPI.html",name=userID.get()['name'],id=userID.key)


@app.route('/addNewAPI/<userID>', methods=['GET','POST'])
@app.route('/addNewAPI',methods=['GET','POST'])
def addNewAPI(userID):
    if request.method == 'POST':
        url_end_point = request.form['url']
        port = request.form['port']
        github = request.form['github']
        tests = request.form.getlist('testlist')
        try:
            api = API(url_end_point, port, github, tests)
            time=datetime.datetime.now()
            run = Run(time)
            api.add_run(run)
            ref=db.reference("/Users").child(userID)
            update_user=user(ref.child('name').get(),ref.child('email').get(),ref.child('apiList').get())
            update_user.add_api(api)
            data = update_user.writeToJson()
            db.reference("/Users").child(userID).set(data)
            return allAPI(userID)
        except:
            return render_template('addNewApi.html', id=userID)

    return render_template('addNewApi.html',id=userID)


@app.route('/createUser', methods=['GET','POST'])
def createUser():
    if request.method == 'POST':
        user_name = request.form['name']
        email = request.form['email']
        password = request.form['pass']
        try:
            u=auth.create_user_with_email_and_password(email, password)
            new_user = user(user_name, email)
            data=new_user.writeToJson()
            db.reference("/Users").child(u.get("localId")).set(data)
            return render_template('createUser.html',us='Create Successful')

        except:
            return render_template('createUser.html', us='Please try again')

    return render_template('createUser.html')

@app.route('/APIruns')
def APIruns():
    return render_template("APIruns.html")

