import os

from flask import Flask
# from rq import Queue
# from rq.job import job
from flask_sqlalchemy import SQLAlchemy
from worker import conn


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import developer

@app.route("/")
def hello():
    return os.environ['APP_SETTINGS']


if __name__ == "__main__":
    app.run()
