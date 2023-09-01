from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db
from flask_cors import CORS
import threading
import time

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate("C:/Users/harshit/Documents/filename.json") #get from firebase 
firebase_admin.initialize_app(cred, {
    'databaseURL': ''  #add RealTime Database from firebase 
})

sensor_data = {}  # Initialize sensor_data dictionary

@app.route('/')
def index():
    return render_template('index.html')

def update_sensor_data():
    global sensor_data  # Use the global variable
    while True:
        sensor_ref = db.reference('Sensor')
        sensor_data = sensor_ref.get()
        print(sensor_data)
        time.sleep(10)

@app.route('/api/sensor-data')
def get_sensor_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    update_thread = threading.Thread(target=update_sensor_data)
    update_thread.start()
    app.run(debug=True)
