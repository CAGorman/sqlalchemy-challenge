# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

print(Base.classes.keys())

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



# # #################################################
# # # Flask Routes
# # #################################################

@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br />"
        f"/api/v1.0/stations<br />"
        f"/api/v1.0/tobs<br />"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"The start and end date should be in the format MMDDYYYY"
    )



# Precipitation 
@app.route("/api/v1.0/precipitation")
def precip():
    session = Session(engine)
  

    precip = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= dt.date(2016,8,23)).order_by(Measurement.date.desc()).all()

    session.close()

    # Create dictionary
    precip_annual = []
    for date, prcp in precip:
        precip_dict = {}
        precip_dict[date] = prcp
        precip_annual.append(precip_dict)
    
    # JSONify list
        return jsonify(precip_annual)




# Stations Page
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    stations = session.query(Station.station).all()

    session.close()
    
    station_list = list(np.ravel(stations))

    
    # JSONify list
    return jsonify(stations = station_list)



# Tobs
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == "USC00519281").filter(Measurement.date >= dt.date(2016,8,18)).all()

    session.close()

    tobs_info = list(np.ravel(tobs))


    # JSONify list
    return jsonify(tobs_info) 


#Start

@app.route("/api/v1.0/<start>")
def trip(start):
    session = Session(engine)
    
    start_date = dt.datetime.strptime(start,"%m%d%Y")

    
    query_data = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.round(func.avg(Measurement.tobs))).\
    filter(Measurement.date >= start_date).all()

    session.close()

    result = list(np.ravel(query_data))

    return jsonify(result)



# Start/End
@app.route("/api/v1.0/<start>/<end>")
def trip2(start, end):
    session = Session(engine)

    start_date = dt.datetime.strptime(start,"%m%d%Y")
    end_date = dt.datetime.strptime(end,"%m%d%Y")

    query_result = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.round(func.avg(Measurement.tobs))).\
    filter(Measurement.date.between(start_date,end_date)).all()

    # query_result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    #     filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    
    session.close()

    start_end = list(np.ravel(query_result))

    #Create dictionary
    # start_end_stats = []
    # for min, avg, max in query_result:
    #     trip_dict = {}
    #     trip_dict["Min"] = min
    #     trip_dict["Average"] = avg
    #     trip_dict["Max"] = max
    #     trip_stats.append(trip_dict)

    # JSONify list
    return jsonify(start_end) 




if __name__ == '__main__':
    app.run(debug=True)