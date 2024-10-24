from flask import Flask,request,jsonify,render_template,url_for
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

## import ridge regression and StandardScalar
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
scalar=pickle.load(open('models/scalar.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        temperature=int(request.form.get('temperature'))
        rh=int(request.form.get('rh'))
        ws=int(request.form.get('ws'))
        rain=float(request.form.get('rain'))
        ffmc=float(request.form.get('ffmc'))
        dmc= float(request.form.get('dmc'))
        isi=float(request.form.get('isi'))
        classes=int(request.form.get('classes'))
        region=int(request.form.get('region'))
        
        new_data_scaled=scalar.transform([[temperature,rh,ws,rain,ffmc,dmc,isi,classes,region]])
        result=ridge_model.predict(new_data_scaled)
        
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
    