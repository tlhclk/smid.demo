# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from person_panel.models import PersonIDInfoModel
import json,datetime
from user_panel.models import UserCompanyModel,CompanyInfoModel



# Create your views here.
def birthday_calendar(request):
    student_list=PersonIDInfoModel.objects.filter(company_id=request.user.company_id_id).order_by('birth_day')
    json_list=[]
    birthday_list=[]
    for student in student_list:
        if student.birth_day:
            birthday_list.append((student.full_name(),student.birth_day))
            json_list.append([student.full_name(),'%d-%d-%d' %(datetime.datetime.today().year,student.birth_day.month,student.birth_day.day+1),'%d-%d-%d' %(datetime.datetime.today().year,student.birth_day.month,student.birth_day.day+1),True])
    return render(request,'calendar_panel/calendar.html',{'birthday_json':json.dumps(json_list),'title':'Doğum Günü Takvimi'})

def graph(request):
    return render(request,'calendar_panel/graphic.html')
