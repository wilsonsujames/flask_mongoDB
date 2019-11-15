from flask import Flask, jsonify, render_template, request

from werkzeug.utils import secure_filename

import os
import pymongo


app = Flask(__name__)





@app.route('/write',methods=[ "GET",'POST'])
def upload():
    print("write to mongoDB")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]   

    mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
    mycol.insert_many(mylist)
    print("done")


    return index()

@app.route('/')
def index():
    return render_template('index.html')
	
	

if __name__ == "__main__":
    app.run(debug=True)	