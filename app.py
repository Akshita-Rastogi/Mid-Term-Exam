from flask import Flask, redirect, url_for, request,render_template
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
  

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,9)
    loaded_model = pickle.load(open("midterm_decision_model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result


@app.route("/")
def index():
    return render_template("index.html"); 
@app.route('/result',  methods =["GET", "POST"])
def result():
    if request.method == "POST":
       
       CreditScore = request.form.get("CreditScore")
       Geography= request.form.get("Geography")

       # getting input with name = lname in HTML form 
       Gender = request.form.get("Gender") 
       Age= request.form.get("Age") 
       Tenure= request.form.get("Tenure") 
       Balance= request.form.get("Balance") 
       HasCrCard= request.form.get("HasCrCard") 
       IsActiveMember = request.form.get("IsActiveMember") 
       EstimatedSalary = request.form.get("EstimatedSalary") 
       l1=[CreditScore,Geography,Gender,Age,Tenure,Balance,HasCrCard,IsActiveMember,EstimatedSalary]
       answer = ValuePredictor(l1)
    return render_template("result.html",Age=answer)
   
  
if __name__ == '__main__':
   app.run(debug = True)