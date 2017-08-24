# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from person_panel.models import PersonIDInfoModel
import json
from user_panel.models import UserCompanyModel,CompanyInfoModel


# Create your views here.
def birthday_calendar(request):
    student_list=PersonIDInfoModel.objects.filter(company_id=CompanyInfoModel.objects.get(pk=UserCompanyModel.objects.get(pk=request.user.id).company_id)).order_by('s_birthday')
    json_list=[]
    birthday_list=[]
    for student in student_list:
        if student.s_birthday:
            birthday_list.append((student.full_name(),student.s_birthday))
            json_list.append({'title':student.full_name(),'start':'%d-%d-%d' %(2017,student.s_birthday.month,student.s_birthday.day+1),'end':'%d-%d-%d' %(2017,student.s_birthday.month,student.s_birthday.day+1),'allDay':True})
    return render(request,'calendar_panel/calendar.html',{'birthday_json':json.dumps(json_list),'title':'Doğum Günü Takvimi'})

def graph(request):
    return render(request,'calendar_panel/graphic.html')
