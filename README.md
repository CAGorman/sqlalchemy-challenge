# sqlalchemy-challenge
Module 10
  In this challenge, You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a     
  climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.This challenge is composed of two 
  parts that are found in the "SurfsUp" folder:
    1. Analyzing and exploring the climate data (app.py)
    2. Designing a climate app (climate_starter.ipynb

## Part 1: 
 This is a jupyter notebook that is broken down into 4 sections:
   1. Importing dependencies
   2. Reflecting Tables into SQLAlchemy ORM - where we create an engine to hawaii.sqlite , reference the tables, and crete the session link from Python to the 
      DB
   3. Exploratory Precipitation Analysis- here we design a query to retrieve the last 12 months of precipitation data and then plot the results in a graph
   4. Exploratory Station Analysis - finally we design a query to calculate the total number of stations in the dataset, locate the mose active station id, and then plot the temperature observations of this station for the past 12 months

## Part 2:
In the second part aFlask API is designed based on the queries that were just developed. To do so, Flask was used to create your routes as follows:
  1. Start the homepage and list all available routes
  2. /api/v1.0/precipitation
  3. /api/v1.0/stations
  4. /api/v1.0/tobs
  5. /api/v1.0/<start> and /api/v1.0/<start>/<end>
