# -*- import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(_name_)
model= pickle.load(open('mining.pkl','rb'))

              
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return  render_template("about.html")
@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering    results on HTML GUI
    '''
    
    x_test = [[x for x in request.form.values()]]
    prediction = model.predict(x_test)
    pred=prediction[0]
    print(prediction)

    
    
    return render_template('index.html', prediction_text='Predicted Quality:{}'.format(pred))

    

if _name_ == "_main_":
    app.run(debug=pickle.FALSE)


