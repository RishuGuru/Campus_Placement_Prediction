from django.shortcuts import render
import joblib
import pandas as pd
# import numpy as np
# Create your views here.
def convert(x):
    if x == 'on':
        return 1
    else:
        return 0
def home(request):
    model = joblib.load("model_xy.sav")
    col_name = ['ssc_p', 'hsc_p', 'degree_p', 'etest_p', 'mba_p', 'gender_M',
       'ssc_b_Central', 'hsc_b_Central', 'hsc_s_Arts', 'hsc_s_Commerce',
       'hsc_s_Science', 'degree_t_Comm&Mgmt', 'degree_t_Others',
       'degree_t_Sci&Tech', 'workex_Yes', 'specialisation_Mkt&Fin',
       'specialisation_Mkt&HR']
    if request.method =='GET':
        return render(request,"home.html")        
    else:
        ssc_p = request.POST.get('ssc_p')
        hsc_p = request.POST.get('hsc_p')
        degree_p = request.POST.get('degree_p')
        etest_p = request.POST.get('etest_p')
        mba_p = request.POST.get('mba_p')
        gender_M = request.POST.get('gender_M')
        ssc_b_Central = request.POST.get('ssc_b_Central')
        hsc_b_Central = request.POST.get('hsc_b_Central')
        hsc_s_Arts = request.POST.get('hsc_s_Arts')
        hsc_s_Arts = convert(hsc_s_Arts)

        hsc_s_Commerce = request.POST.get('hsc_s_Commerce')
        hsc_s_Commerce = convert(hsc_s_Commerce)

        hsc_s_Science = request.POST.get('hsc_s_Science')
        hsc_s_Science = convert(hsc_s_Science)

        degree_t_Comm_Mgmt = request.POST.get('degree_t_Comm&Mgmt')
        degree_t_Comm_Mgmt = convert(degree_t_Comm_Mgmt)
        degree_t_Others = request.POST.get('degree_t_Others')
        degree_t_Others = convert(degree_t_Others)
        degree_t_Sci_Tech = request.POST.get('degree_t_Sci&Tech')
        degree_t_Sci_Tech = convert(degree_t_Sci_Tech)
        workex_Yes = request.POST.get('workex_Yes')
        specialisation_Mkt_Fin = request.POST.get('specialisation_Mkt&Fin')
        specialisation_Mkt_Fin = convert(specialisation_Mkt_Fin)

        specialisation_Mkt_HR = request.POST.get('specialisation_Mkt&HR')
        specialisation_Mkt_HR = convert(specialisation_Mkt_HR)
        # print(ssc_p,hsc_p,degree_p,etest_p,mba_p,gender_M,ssc_b_Central,
        # hsc_b_Central,hsc_s_Arts,hsc_s_Commerce,hsc_s_Science,degree_t_Comm_Mgmt,
        # degree_t_Others,degree_t_Sci_Tech,workex_Yes,specialisation_Mkt_Fin,specialisation_Mkt_HR)
        
        xyz = pd.DataFrame([[ssc_p,hsc_p,degree_p,etest_p,mba_p,int(gender_M),int(ssc_b_Central),
            int(hsc_b_Central),hsc_s_Arts,hsc_s_Commerce,hsc_s_Science,degree_t_Comm_Mgmt,
            degree_t_Others,degree_t_Sci_Tech,int(workex_Yes),specialisation_Mkt_Fin,specialisation_Mkt_HR]],
                        columns=col_name)

        pred = model.predict(xyz)
        if pred[0]==0:
            message = 'Not Placed'
        else:
            message = 'Placed'
        return render(request,"home.html",{"message":message})
        