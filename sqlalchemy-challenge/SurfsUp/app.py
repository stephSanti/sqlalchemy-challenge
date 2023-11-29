import numpy as np
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import func
from sqlalchemy import and_
from datetime import datetime, timedelta

app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///C:\\Users\\Madelyn Zelaya\\Desktop\\Module10\\Starter_Code\\Resources\\hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all precipation queries"""
    # Query
    results = session.query(Measurement.prcp).all()

    session.close()


    # Convert list of tuples into normal list
    precip_data = list(np.ravel(results))

    

#     Return the JSON representation of your dictionary.
    return jsonify(precip_data)

@app.route("/api/v1.0/stations")
def stations():
    active_stations = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).\
    all()
    
    return jsonify()

app.run()
