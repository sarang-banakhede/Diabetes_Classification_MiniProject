import pandas as pd
from flask import Flask ,request,render_template,jsonify
import pickle

app=Flask(__name__)

model=pickle.load(open('Diabities classification Project\Model\model.pkl','rb'))


@app.route("/")
def Home():
    return render_template("Home.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    Pregnancies=request.form.get('Pregnancies')
    Glucose=request.form.get('Glucose')
    BloodPressure=request.form.get('BloodPressure')
    SkinThickness=request.form.get('SkinThickness')
    Insulin=request.form.get('Insulin')
    BMI=request.form.get('BMI')
    DiabetesPedigreeFunction=request.form.get('DiabetesPedigreeFunction')
    Age=request.form.get('Age')
    
    final_list=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    df=pd.DataFrame([final_list])
    prediction=model.predict(df)
    if prediction==1:
        prediction='probably you have diabetes please consult with your doctor 😔'
    else:
        prediction='probably you dont have diabetes 😃'
    
    return render_template('home.html',predict=prediction)

if __name__=='__main__':
    app.run(debug=True)