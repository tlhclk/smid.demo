# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from person_panel.models import PersonIDInfoModel
import json

# Create your views here.
def birthday_calendar(request):
    student_list=PersonIDInfoModel.objects.all()
    json_list=[]
    birthday_list=[]
    for student in student_list:
        if student.s_birthday:
            birthday_list.append((student.full_name(),student.s_birthday))
            json_list.append({'title':student.full_name(),'start':'%d-%d-%d' %(2017,student.s_birthday.month,student.s_birthday.day),'end':'%d-%d-%d' %(2017,student.s_birthday.month,student.s_birthday.day),'allDay':True})

    birthday_json=open('static/birthday_list.json','w+',encoding='utf8')
    birthday_json.write(json.dumps(json_list,indent=4,sort_keys=True,separators=(',', ': '), ensure_ascii=False,))
    birthday_json.close()
    return render(request,'calendar_panel/calendar.html')

def graph(request):
    return render(request,'calendar_panel/graphic.html')
