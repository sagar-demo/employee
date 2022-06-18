from flask import Flask,request,render_template

import sklearn

import  pickle

import numpy as np

app=Flask(__name__)
model=pickle.load(open('Hr_salary.pkl','rb'))


@app.route('/')
@cross_origin()
def home():
    return render_template("index1.html")


@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    Department_RandD=0
    if request.method=="POST":

        satisfaction_level=float(request.form['satisfaction_level'])
        last_evaluation=float(request.form['last_evaluation'])
        number_project=int(request.form['number_project'])
        average_montly_hours=int(request.form['average_montly_hours'])
        time_spend_company=int(request.form['time_spend_company'])
        Work_accident=int(request.form['Work_accident'])
        promotion_last_5years=int(request.form['promotion_last_5years'])
        Department=request.form['Department']
        if(Department=='Department_RandD'):
            Department_RandD=1
            Department_hr=0
            Department_accounting=0
            Department_management=0
            Department_marketing=0
            Department_product_mng=0
            Department_sales=0
            Department_support=0
            Department_technical=0
        elif(Department=='Department_hr'):
            Department_RandD=0
            Department_hr=1
            Department_accounting=0
            Department_management=0
            Department_marketing=0
            Department_product_mng=0
            Department_sales=0
            Department_support=0
            Department_technical=0
        elif(Department=='Department_management'):
            Department_RandD=0
            Department_hr=0
            Department_accounting=0
            Department_management=1
            Department_marketing=0
            Department_product_mng=0
            Department_sales=0
            Department_support=0
            Department_technical=0
        elif(Department=='Department_accounting'):
            Department_RandD=0
            Department_hr=0
            Department_accounting=1
            Department_management=0
            Department_marketing=0
            Department_product_mng=0
            Department_sales=0
            Department_support=0
            Department_technical=0
        elif(Department=='Department_marketing'):
            Department_RandD=0
            Department_hr=0
            Department_accounting=0
            Department_management=0
            Department_marketing=1
            Department_product_mng=0
            Department_sales=0
            Department_support=0
            Department_technical=0
        elif(Department=='Department_product_mng'):
            Department_RandD=0
            Department_hr=0
            Department_accounting=0
            Department_management=0
            Department_marketing=0
            Department_product_mng=1
            Department_sales=0
            Department_support=0
            Department_technical=0
        elif(Department=='Department_sales'):
            Department_RandD=0
            Department_hr=0
            Department_accounting=0
            Department_management=0
            Department_marketing=0
            Department_product_mng=0
            Department_sales=1
            Department_support=0
            Department_technical=0
        elif(Department=='Department_support'):
            Department_RandD=0
            Department_hr=0
            Department_accounting=0
            Department_management=0
            Department_marketing=0
            Department_product_mng=0
            Department_sales=0
            Department_support=1
            Department_technical=0
        elif(Department=='Department_technical'):
            Department_RandD=0
            Department_hr=0
            Department_accounting=0
            Department_management=0
            Department_marketing=0
            Department_product_mng=0
            Department_sales=0
            Department_support=0
            Department_technical=1
        else:
            Department_RandD=0
            Department_hr=0
            Department_accounting=0
            Department_management=0
            Department_marketing=0
            Department_product_mng=0
            Department_sales=0
            Department_support=0
            Department_technical=0

        # salary
        salary=request.form['salary']
        if(salary=='salary_low'):
            salary_low=1
            salary_medium=0

        elif(salary=='salary_medium'):
            salary_low=0
            salary_medium=1

        # elif(salary=='salary_high'):
        #     salary_low=0
        #     salary_medium=0
        #     salary_high=1
        else:
            salary_low=0
            salary_medium=0
            # salary_high=0

        prediction=model.predict([[
            satisfaction_level,
            last_evaluation,
            number_project,
            average_montly_hours,
            time_spend_company,
            Work_accident,
            promotion_last_5years,
            salary_low ,
            salary_medium,

            Department_RandD,
            Department_hr,
            Department_management,
            Department_accounting,
            Department_marketing,
            Department_product_mng,
            Department_sales,
            Department_technical,
            Department_support




        ]])
        output=round(prediction[0],2)
        return render_template('index1.html',prediction_text='Employee prediction is (0 Not Left 1 Left)= {}'.format(output))
    return render_template('index1.html')







        #





if __name__ == "__main__":
    app.run(debug=True)
