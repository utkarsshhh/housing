#!/usr/bin/env python3.7
import flask
from flask_cors import CORS, cross_origin
import json
from flask import request,jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
ld = open('db.json')
db = json.load(ld)
ld.close()
import joblib
import pandas as pd


@app.route('/users', methods=['GET'])
@cross_origin()
def login():
    return jsonify(db)

@app.route('/users/register',methods=['GET','POST'])
@cross_origin()
def register():
    if(request.method=='GET'):
        return db
    elif(request.method=='POST'):
        ld = open('db.json')
        db_2 = json.load(ld)
        updated = request.get_json()
        db_2['users'].append(updated)
        ld.close()
        lw = open('db.json','w')
        json.dump(db_2,lw)
        lw.close()
        return jsonify(db_2)

@app.route('/users/predict',methods = ['POST'])
@cross_origin()
def predict():
    pred_vals = request.get_json()
    print (pred_vals)
    model = joblib.load('model.pkl')
    x_pred = pd.DataFrame(pred_vals,(1,))
    response = model.predict(x_pred)
    return jsonify(response.tolist())
if __name__ == '__main__':
    app.run()
