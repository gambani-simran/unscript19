import os                       
import json                       
import datetime                       
from flask import Flask, render_template,request,redirect,url_for # For flask implementation
#from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient

app = Flask(__name__)
title = "App for patients"  
heading = "Medical help-chat app for patients"

client = MongoClient("mongodb://127.0.0.1:27017") #host uri
#db = client.mymongodb #Select the database
#coll = db.coll #Select the collection name
 
@app.route("/")
def hello():
	return "Hey!"
 
if __name__ == "__main__":
	app.run()