import json
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from .utils import load_and_store_data
from bson import ObjectId
from flask_cors import CORS 

# Custom JSON encoder for MongoDB ObjectId
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

# Initialize Flask app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/university"
mongo = PyMongo(app)

# Set the custom JSON encoder
app.json_encoder = JSONEncoder

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}}) 

# Scheduler to reload data every 10 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(func=load_and_store_data, args=[mongo], trigger="interval", minutes=10)
scheduler.start()

# Ensure data is loaded at startup
load_and_store_data(mongo)

# Shutdown scheduler on exit
atexit.register(lambda: scheduler.shutdown())

# Import routes
from .routes import *

if __name__ == "__main__":
    app.run(debug=True)
