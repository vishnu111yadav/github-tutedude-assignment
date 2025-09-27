from flask import Flask  , render_template , request
import requests
from datetime import datetime

BACKEND_URL = 'http://0.0.0.0:9000'

app = Flask(__name__)

@app.route('/')
def home():
     day =datetime.today().strftime('%A')+ " " + datetime.today().strftime('%B') + " " + datetime.today().strftime('%d')
     current_time = datetime.now().strftime("%H:%M:%S")
     # return "Today is" + day
     return render_template('index.html', day=day,current_time=current_time)

@app.route('/submit' , methods=['POST'])
def submit():

    form_data = dict(request.form)

    requests.post(BACKEND_URL + '/submit' ,json=form_data)

    return "Data submitted successfully"

@app.route('/get_data')
def get_data():

   response = requests.get(BACKEND_URL + '/view')

   return response.json()

if __name__ == "__main__":
      app.run(host='0.0.0.0' , port=8000 , debug=True)