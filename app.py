import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model1 = pickle.load(open('model_next_week.pkl', 'rb'))
model2 = pickle.load(open('model_next_4_weeks.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
   
    from datetime import datetime, date
    Store=int(request.form['Store'])
    Curr_Week_sale=int(request.form['sales in Current Week'])
    dt = datetime.strptime(request.form['Date'],'%Y-%m-%d')
    week=dt.strftime("%V")
    month=int(dt.strftime("%m"))
    if month in [1,2,3]:
        Q=4
    else:
        Q= (month-4)//3 +1  
    prediction = model1.predict([[Store,Curr_Week_sale,week,Q]]).sum()
    output1 = round(prediction, 2)
    prediction = model2.predict([[Store,Curr_Week_sale,week,Q]]).sum()
    output2 = round(prediction, 2)

    return render_template('index.html', prediction_text_week='Next week Sales should be $ {}'.format(output1),prediction_text_mon='Next 4-week Sales should be $ {}'.format(output2))


if __name__ == "__main__":
    app.run()