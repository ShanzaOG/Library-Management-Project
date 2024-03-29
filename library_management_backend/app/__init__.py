import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from flask_cors import CORS

# Get values from environment variables
load_dotenv()
url = os.getenv("DATABASE_URL")

# Create an insance of flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://kBWJrUi2G2:9WWS@kBWJrUi2G2@localhost:5432/postgres'
db = SQLAlchemy(app)
CORS(app)

# We import routes and models
from app import models, routes
