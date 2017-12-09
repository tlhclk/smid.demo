# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from person_panel.models import PersonIDInfoModel
import json,datetime
from .forms import EventInfoForm
from .models import EventInfoModel



# Create your views here.
def birthday_calendar(request):
    student_list=PersonIDInfoModel.objects.filter(company_id=request.user.company_id_id).order_by('birth_day')
    json_list=[]
    birthday_list=[]
    for student in student_list:
        if student.birth_day:
            birthday_list.append((student.full_name(),student.birth_day))
            json_list.append([student.full_name(),
                              '%d-%d-%d' %(datetime.datetime.today().year,student.birth_day.month,student.birth_day.day),
                              '%d-%d-%d' %(datetime.datetime.today().year,student.birth_day.month,student.birth_day.day),True])
    return render(request,'calendar_panel/calendar.html',{'birthday_json':json.dumps(json_list),'title':'Takvim'})

def graph(request):
    return render(request,'calendar_panel/graphic.html')

def calendar(request):
    all_events=EventInfoModel.objects.filter(company_id=request.user.company_id_id)
    json_list = []
    for event in all_events:
        if event.all_day:
            json_list.append([event.name,
                              '%d-%d-%d' %(event.start_time.year,event.start_time.month,event.start_time.day),
                              event.all_day,event.type])
        else:
            json_list.append([event.name,
                              '%d-%d-%d' %(event.start_time.year,event.start_time.month,event.start_time.day),
                              '%d-%d-%d' %(event.end_time.year,event.end_time.month,event.end_time.day+1),
                              event.type])
    return render(request, 'calendar_panel/asd.html', {'birthday_json': json.dumps(json_list), 'title': 'Takvim'})