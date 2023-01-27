from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np

app = Flask(__name__, template_folder='templates')

@app.route("/")
def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'.\artifacts\heart_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/predict_heart', methods = ["POST"])

def predict():  
    cp = request.form['cp']  #see data in the website
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang'] 
    
    if request.method == "POST":
        
        to_predict_list = [cp,trestbps,chol,fbs,restecg,thalach,exang]
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "Sorry you have chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    res = str(result)
    return{'result':prediction, 'val': res}

if __name__ == "__main__":
    app.run(debug=True)