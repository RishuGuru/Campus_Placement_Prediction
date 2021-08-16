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
        hsc_s_D = request.POST.get('shs_D')
        if hsc_s_D =='A':
            hsc_s_Arts = 1
            hsc_s_Commerce = 0
            hsc_s_Science = 0
        elif hsc_s_D =='C':
            hsc_s_Arts = 0
            hsc_s_Commerce = 1
            hsc_s_Science = 0
        else:
            hsc_s_Arts = 0
            hsc_s_Commerce = 0
            hsc_s_Science = 1
        degree = request.POST.get('degree')
        if degree =='CM':
            degree_t_Comm_Mgmt = 1
            degree_t_Others = 0
            degree_t_Sci_Tech = 0
        elif degree =='ST':
            degree_t_Comm_Mgmt = 0
            degree_t_Others = 0
            degree_t_Sci_Tech = 1
        else:
            degree_t_Comm_Mgmt = 0
            degree_t_Others = 1
            degree_t_Sci_Tech = 0
        workex_Yes = request.POST.get('workex_Yes')
        Specialization = request.POST.get('Specialization')
        if Specialization== "MF":
            specialisation_Mkt_Fin = 1
            specialisation_Mkt_HR = 0
        elif Specialization== "MF":
            specialisation_Mkt_Fin = 1
            specialisation_Mkt_HR = 0
        else:
            specialisation_Mkt_Fin = 0
            specialisation_Mkt_HR = 0
        # print(ssc_p,hsc_p,degree_p,etest_p,mba_p,gender_M,ssc_b_Central,
        # hsc_b_Central,hsc_s_Arts,hsc_s_Commerce,hsc_s_Science,degree_t_Comm_Mgmt,
        # degree_t_Others,degree_t_Sci_Tech,workex_Yes,specialisation_Mkt_Fin,specialisation_Mkt_HR)
        
        xyz = pd.DataFrame([[ssc_p,hsc_p,degree_p,etest_p,mba_p,int(gender_M),int(ssc_b_Central),
            int(hsc_b_Central),hsc_s_Arts,hsc_s_Commerce,hsc_s_Science,degree_t_Comm_Mgmt,
            degree_t_Others,degree_t_Sci_Tech,int(workex_Yes),specialisation_Mkt_Fin,specialisation_Mkt_HR]],
                        columns=col_name)

        pred = model.predict(xyz)
        
        return render(request,"home.html",{'message':pred[0]})
        