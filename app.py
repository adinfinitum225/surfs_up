import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create engine to connect to database
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()

Base.prepare(engine, reflect=True)

# Create variables for our tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Get a session to use for queries
session = Session(engine)

# Set up Flask
app = Flask(__name__)

@app.route('/')

def welcome():
    return(
            f'Welcome to the Climate Analysis API!'
            f'<br>Available Routes:'
            f'<br>/api/v1.0/precipitation'
            f'<br>/api/v1.0/stations'
            f'<br>/api/v1.0/tobs'
            f'<br>/api/v1.0/temp/start/end'
            )

@app.route('/api/v1.0/precipitation')

def precipitation():
    return
