"""
Main program run file


"""
import json

from flask import Flask, render_template,url_for

import testBRTFRC
import testDOS
import testJSONJCTN
import testXSS
from test_resaults import TestRes

app = Flask(__name__)

# config = {
#     "apiKey": "AIzaSyCNmdtg0fjdCXoXXkUSxqSiIYuzl_50R4Y",
#     "authDomain": "finalproject-71cb6.firebaseapp.com",
#     "projectId": "finalproject-71cb6",
#     "databaseURL": "https://finalproject-71cb6-default-rtdb.firebaseio.com/",
#     "storageBucket": "finalproject-71cb6.appspot.com",
#     "messagingSenderId": "463492559459",
#     "appId": "1:463492559459:web:8f42ae5c51143311703e56",
#     "measurementId": "G-DKJWRJQHP1"
# }


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

@app.route('/login')
def login():
    return render_template("login.html")

#שליפה של כל הAPI של המשתמש הספציפי והעברה של המידע לHTML
@app.route('/allAPI')
def allAPI():
    return render_template("allAPI.html")

@app.route('/addNewAPI')
def addNewAPI():
    return render_template("addNewApi.html")




