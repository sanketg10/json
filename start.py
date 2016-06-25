
# from flask import Flask, render_template 
# from test_flask import app 

import urllib2 
import json 

# app = Flask(__name__)


# @app.route("/")


def printResults(data): 
    theJSON = json.loads(data)  
    print theJSON
    if "title" in theJSON["metadata"]: 
        print theJSON["metadata"]["title"]

def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"

    webUrl  = urllib2.urlopen(urlData) 
    print webUrl.getcode() 
    data = webUrl.read() 

    printResults(data)  


if __name__== "__main__":
  main()
