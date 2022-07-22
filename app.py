# import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# setup database

# allows access to SQLite db file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect db 
Base = automap_base()
Base.prepare(engine, reflect=True)

# create variables for each class
Measurement = Base.classes.measurement
Station = Base.classes.station

# create the session link
session = Session(engine)

# first, define the flask app
app = Flask(__name__)

# then, build the routes
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

# define route for precip data
@app.route("/api/v1.0/precipitation")

# define the year from the date of the last observation
# filter the query on prev_year
# create dict with date as the key and precip as value
# use jsonify fn to convert dict to JSON file
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# create route for stations
@app.route("/api/v1.0/stations")

# query all stations in db
# unravel results into a 1D array using np.ravel()
# convert to list using list()
# convert to JSON file using jsonify()
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# create route for monthly temp
@app.route('/api/v1.0/tobs')

# calculate date
# query all temp obs at the primary station for the prev year
# unravel, convert to list, convert to JSON
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# create tour for stats
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# query to select min, max, ave temp
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)