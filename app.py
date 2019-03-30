from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
from flask import Flask


app = Flask(__name__)

title = "Medical help app"
heading = "Application for medical help"

client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.MedicalApp    #Select the database
pat = db.patients #Select the collection name

def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')

@app.route("/list")
def lists ():
	#Display the all Tasks
	todos_l = pat.find()
	a1="active"
	return render_template('index.html',a1=a1,pat=todos_l,t=title,h=heading)

@app.route("/")
def hello():
	return "welcome"
@app.route("/uncompleted")
def tasks ():
	#Display the Uncompleted Tasks
	todos_l = pat.find({"done":"no"})
	a2="active"
	return render_template('index.html',a2=a2,pat=todos_l,t=title,h=heading)

"""
@app.route("/completed")
def completed ():
	#Display the Completed Tasks
	todos_l = pat.find({"done":"yes"})
	a3="active"
	return render_template('index.html',a3=a3,pat=todos_l,t=title,h=heading)
"""

"""
@app.route("/done")
def done ():
	#Done-or-not ICON
	id=request.values.get("_id")
	task=pat.find({"_id":ObjectId(id)})
	if(task[0]["done"]=="yes"):
		pat.update({"_id":ObjectId(id)}, {"$set": {"done":"no"}})
	else:
		pat.update({"_id":ObjectId(id)}, {"$set": {"done":"yes"}})
	redir=redirect_url()	

	return redirect(redir)
"""

@app.route("/action", methods=['POST'])
def action ():
	#Adding a patient data
	name=request.values.get("name")
	desc=request.values.get("desc")
	date=request.values.get("date")
	pr=request.values.get("pr")
	pat.insert({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})
	return redirect("/list")

@app.route("/remove")
def remove ():
	#Deleting a Task with various references
	key=request.values.get("_id")
	pat.remove({"_id":ObjectId(key)})
	return redirect("/")

@app.route("/update")
def update ():
	id=request.values.get("_id")
	task=pat.find({"_id":ObjectId(id)})
	return render_template('update.html',tasks=task,h=heading,t=title)

@app.route("/action3", methods=['POST'])
def action3 ():
	#Updating a Task with various references
	name=request.values.get("name")
	desc=request.values.get("desc")
	date=request.values.get("date")
	pr=request.values.get("pr")
	id=request.values.get("_id")
	pat.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "desc":desc, "date":date, "pr":pr }})
	return redirect("/")

	"""
	name=request.values.get("name")
	gender=request.values.get("gender")
	dob=request.values.get("dob")
	contact=request.values.get("contact")
	maritalstatus=request.values.get("maritalstatus")
	age=request.values.get("Age")
	photo=request.values.get("photo")

	"""

"""
@app.route("/search", methods=['GET'])
def search():
	#Searching a Task with various references

	key=request.values.get("key")
	refer=request.values.get("refer")
	if(key=="_id"):
		todos_l = pat.find({refer:ObjectId(key)})
	else:
		todos_l = pat.find({refer:key})
	return render_template('searchlist.html',pat=todos_l,t=title,h=heading)
"""

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)


if __name__ == "__main__":

    app.run()
