# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from person_panel.models import PersonIDInfoModel
import json,datetime
from .forms import EventInfoForm
from .models import EventInfoModel

def birthday_calendar(request):
    if request.user.has_perm('calendar_panel.change_eventinfomodel'):
        student_list=PersonIDInfoModel.objects.filter(company=request.user.company_id).order_by('birth_day')
        json_list=[]
        birthday_list=[]
        for student in student_list:
            if student.birth_day:
                birthday_list.append((student.full_name(),student.birth_day))
                json_list.append([student.full_name(),
                                  '%d-%d-%d' %(datetime.datetime.today().year,student.birth_day.month,student.birth_day.day),
                                  '%d-%d-%d' %(datetime.datetime.today().year,student.birth_day.month,student.birth_day.day),True])
        return render(request,'calendar_panel/calendar.html',{'birthday_json':json.dumps(json_list),'title':'Takvim'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def agenda(request):
    if request.user.has_perm('calendar_panel.change_eventinfomodel'):
        today=datetime.date.today()
        person_list=[]
        for person in PersonIDInfoModel.objects.filter(company=request.user.company_id):
            if (person.birth_day.month-today.month)==1:
                if person.birth_day.day<today.day:
                    person_list.append(person)
            elif person.birth_day.month==today.month:
                if person.birth_day.day>=today.day:
                    person_list.append(person)
            elif today.month==12:
                if person.birth_day.month==1:
                    if person.birth_day.day<today.day:
                        person_list.append(person)
        return render(request, 'calendar_panel/agenda.html',{'title':'Ajanda','event_list':person_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def event_calendar(request):
    if request.user.has_perm('event_panel.change_eventinfomodel'):
        all_events=EventInfoModel.objects.filter(company=request.user.company_id)
        json_list = []
        for event in all_events:
            if event.all_day:
                json_list.append([event.name,
                                  '%d-%d-%d' %(event.start_time.year,event.start_time.month,event.start_time.day),
                                  '%d-%d-%d' %(event.start_time.year,event.start_time.month,event.start_time.day),event.all_day])
            else:
                json_list.append([event.name,
                                  '%d-%d-%d' %(event.start_time.year,event.start_time.month,event.start_time.day),
                                  '%d-%d-%d' %(event.end_time.year,event.end_time.month,event.end_time.day+1),event.all_day])
        return render(request, 'calendar_panel/asd.html', {'birthday_json': json.dumps(json_list), 'title': 'Takvim'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def event_add(request,person=None):
    if request.user.has_perm('event_panel.add_eventinfomodel'):
        if person:
            new_event=EventInfoModel(name=person.full_name()+' Doğum Günü',start_time=person.birth_day,end_time=person.birth_day,all_day=True,type='0',desc=str(person.tcn),company=person.company)
            new_event.save()
        else:
            pass
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def event_detail(request):
    pass

def event_edit(request):
    pass

def event_delete(request):
    pass