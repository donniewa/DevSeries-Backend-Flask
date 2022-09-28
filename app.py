from flask import Flask, render_template, url_for, json, jsonify, Response
from flask_cors import CORS
from DataClass import DataClass


app = Flask(__name__)
CORS(app, send_wildcard=True)

my_data = DataClass()

@app.route("/getSomeData")
def getSomeData():
    r = my_data.globalData
    return Response(json.dumps(r), mimetype='application/json')

@app.route("/getSomeDataFromFile")
def getSomeDataFromFile():
    r = my_data.getJsonFromFile('./data/hello.json')
    return Response(json.dumps(r), mimetype='application/json')

@app.route("/getSomeDataArrayFromFile")
def getSomeDataArrayFromFile():
    r = my_data.getJsonFromFile('./data/hello-lots.json')
    return Response(json.dumps(r), mimetype='application/json')

@app.route("/employees")
def employees():
    r = my_data.getJsonFromFile('./data/employees.json')
    return Response(json.dumps(r), mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
