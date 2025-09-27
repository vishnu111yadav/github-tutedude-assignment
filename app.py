from flask import Flask , request , render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')
def home():
     day =datetime.today().strftime('%A')+ " " + datetime.today().strftime('%B') + " " + datetime.today().strftime('%d')
     current_time = datetime.now().strftime("%H:%M:%S")
     # return "Today is" + day
     return render_template('index.html', day=day,current_time=current_time)

@app.route('/second')
def second():
     return "welcome to second page"

@app.route('/api/<name>')
def name(name):
     print(name)
     length =len(name)
     if length>5:
          return "name is too long"
     else:
          return "name is short"
     
@app.route('/add/<a>/<b>')
def add(a,b):
     answer = int(a) + int(b)
     result ={
          'answer':answer
     }
     return result

@app.route('/api')
def user():

     name = request.values.get('name')
     age =  request.values.get('age')

     result ={
          'name':name,
          'age':age
     }
     return result

@app.route('/submit', methods=['POST'])
def submit():
     # name = request.form.get('name')
     form_data = dict(request.form)
     collection.insert_one(form_data)
     return "Insert Succes"

@app.route('/view')
def view():
     data = collection.find()
     data = list(data)
     for item in data:
          del item['_id']
          print(item)

     data = {
          'data':data
     }
     return data

if __name__ == "__main__":
     app.run(debug=True)