# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from stock_panel.models import RoomInfoModel
from person_panel.models import StudentInfoModel
from django.conf.urls.static import static,serve
from django.conf import settings
from account_panel.models import *
from calendar_panel.models import *
from document_panel.models import *
from operation_panel.models import *
from person_panel.models import *
from report_panel.models import *
from stock_panel.models import *
from user_panel.models import *


def home_page(request):
    if str(request.user)!='AnonymousUser':
        total=sum([int(room.people) for room in RoomInfoModel.objects.filter(company=request.user.company_id)])
        registred = len(StudentInfoModel.objects.filter(company=request.user.company_id))# TODO: ajaxa dönücek
        return render(request,'home_page.html',{'title':'Ana Sayfa','empty':total - registred,'registred':registred})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def main_page(request):
    return render(request,'main_page.html',{'title':'Ana Sayfa'})

def contract(request):
    return render(request,'contract.html',{'title':'Sözleşme'})

def rules(request):
    return render(request, 'rules.html', {'title': 'Kurallar'})

def termofuse(request):
    return render(request, 'termofuse.html', {'title': 'Kullanım Koşulları'})

def page_not404_found(request):
    response= render(request,'404.html',{'title':'404 Not Found'})
    response.status_code=404
    return response

def page_not403_found(request):
    response= render(request,'403.html',{'title':'403 Forbidden'})
    response.status_code=403
    return response

def page_not400_found(request):
    response= render(request,'400.html',{'title':'400 Bad Request'})
    response.status_code=400
    return response

def page_not500_found(request):
    response= render(request,'500.html',{'title':'500 Internal Server Error'})
    response.status_code=500
    return response

def media_view(request,path):
    if request.user.id:
        return serve(request,path,settings.MEDIA_ROOT,)
    else:
        return serve(request,path,settings.MEDIA_ROOT)
        #return page_not404_found(request)

def static_view(request,path):
    return serve(request,path,settings.STATIC_ROOT)
