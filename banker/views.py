from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
# from sklearn.preprocessing import StandardScaler
# from sklearn.impute import SimpleImputer

import numpy as np
import os
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
url1 = staticfiles_storage.url('models\model_pickle1')
file_path1 = os.path.join(settings.STATIC_ROOT, 'models/model_pickle1')
url2 = staticfiles_storage.url('models\model_pickle2')
file_path2 = os.path.join(settings.STATIC_ROOT, 'models/model_pickle2')
# Create your views here.
sc1,model1 = pd.read_pickle(file_path1)
sc2,le2,model2 = pd.read_pickle(file_path2)
# sc = StandardScaler()
# imputer = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def instruct(request):
    return render(request, 'instruction.html')

def submit(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        bname = request.POST.get('bName')
        license = request.POST.get('license')
        # print(year)
        # print(request.POST.get('income'))
        income = float(request.POST.get('income'))
        expenditure = float(request.POST.get('expenditure'))
        npa = float(request.POST.get('npa'))
        dividend = float(request.POST.get('dividend'))
        candl = float(request.POST.get('candl'))

        if license=='no':
            return render(request,'results.html',{'result':0})
        # print(year,bname,license,income,expenditure,npa,dividend,candl)
        temp={}
        net_profit = income - expenditure
        threshold_npa = (npa/income)*100
        if dividend>0:
            div_class = 1
        else:
            div_class = 0
        profit_per = (net_profit/income)*100

        if threshold_npa<9 and threshold_npa>=6:
            npa_class=1
        elif threshold_npa<12 and threshold_npa>=9:
            npa_class=2
        elif threshold_npa<15 and threshold_npa>=12:
            npa_class=3
        else:
            npa_class=4
        # temp['year']=year
        # temp['bname']=bname
        # temp['license']=license
        temp['income']=income
        temp['expenditure']=expenditure
        temp['npa']=npa
        temp['dividend']=dividend
        temp['net_profit']=net_profit
        temp['candl']=candl
        temp['threshold_npa']=threshold_npa
        temp['div_class']=div_class
        temp['profit_per']=profit_per
        temp['npa_class']=npa_class

        # print("##############################################")
        # print(temp)
        # with open(r'C:\Users\Office\PycharmProjects\machinelearning\models\model_pickle','rb') as f:
        #     mp=pickle.load(f)
        vals = np.array(list(temp.values()))
        testData=pd.DataFrame({'x':temp}).transpose()
        vals = sc1.transform([vals])
        # print(testData)
        # testData = imputer.fit_transform(testData)
        # testData = sc.fit_transform(testData)
        # print("***************************************")
        # score = model.predict([[265100.1	,	271647.46, 110855, 0, -6547.4, 3454752, 41.8161668, 0, -2.469768967, 4]])
        # print(score)
        #scoreval=model.predict([[temp['income'],temp['expenditure'],temp['npa'],temp['dividend'],temp['net_profit'],temp['candl'],temp['threshold_npa'],temp['div_class'],temp['profit_per'],temp['npa_class']]])
        scoreval = model1.predict(vals)
        # print(scoreval)

        temp['target']=scoreval
        temp['target'] = le2.transform(temp['target'])
        # print("*********************************************")
        # print(temp)
        # with open(r'C:\Users\Office\PycharmProjects\machinelearning\models\model_pickle','rb') as f:
        #     mp=pickle.load(f)
        vals1 = np.array(list(temp.values()))
        testData1=pd.DataFrame({'x':temp}).transpose()
        vals1 = sc2.transform([vals1])
        # print(testData1)
        # print(type(testData1.iloc[:,:].values))
        # print(type(temp))
        # testData1 = imputer.fit_transform(testData1)
        # testData1 = sc.fit_transform(testData1)
        # print("***************************************")
        #scoreval1=model1.predict([[temp['income'],temp['expenditure'],temp['npa'],temp['dividend'],temp['net_profit'],temp['candl'],temp['threshold_npa'],temp['div_class'],temp['profit_per'],temp['npa_class'],temp['target']]])
        scoreval1 = model2.predict(vals1)
        # print(scoreval1)
        npabar = threshold_npa*3
        profitbar = abs(profit_per*3)
        classbar = npa_class*20
        return render(request,'results.html',{'result':scoreval1[0],'divClass':scoreval[0],'npa':int(threshold_npa),'profit':int(profit_per),'class':npa_class,'npa_bar':npabar,'profit_bar':profitbar,'class_bar':classbar,'bname':bname})
       # context={'scoreval':scoreval,'temp':temp}
       # print(context)
       # classification=scoreval[0]
    else:
        render(request,'instrucion.html')