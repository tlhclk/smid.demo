# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from stock_panel.models import RoomInfoModel
from person_panel.models import StudentInfoModel
from django.conf.urls.static import static,serve
from django.conf import settings
import xlrd
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
#     model_list=[AccountInfoModel,PersonAssetInfoModel,PeriodicPaymentModel,TransactionInfoModel,BillInfoModel,
#                 EventInfoModel,
#                 DocumentInfoModel,LiabilityInfoModel,
#                 StudentLeaveModel,AttendanceInfoModel,VacationInfoModel,NotificationInfoModel,
#                 PersonIDInfoModel,PersonalInfoModel,StudentInfoModel,ParentInfoModel,
#                 RoomInfoModel,FixtureInfoModel,
#                 ]
#     file =open('dormoni/database_csv.txt','r',encoding='utf-8')
#     field_list=[]
#     for line in file:
#         line_list=line.split(',')
#         if line_list[0]=='Model':
#             field_list=line_list[1:]
        # elif line_list[0]==str(model_list[0]):#account_info
        #     company=CompanyInfoModel.objects.get(pk=line_list[7])
        #     new=AccountInfoModel(no=line_list[1],name=line_list[2],type=line_list[3],amount=line_list[4],desc=line_list[5],bank_code=line_list[6],company=company)
        #     new.save()
        # elif line_list[0]==str(model_list[1]):#Personasset
        #     company=CompanyInfoModel.objects.get(pk=line_list[7])
        #     person=StudentInfoModel.objects.get(pk=line_list[1])
        #     new=PersonAssetInfoModel(person=person,debt=line_list[3],desc=line_list[4],period=line_list[5],type=line_list[6],company=company)
        #     new.save()
        # elif line_list[0]==str(model_list[2]):#Periodicpayment
        #     company=CompanyInfoModel.objects.get(pk=line_list[17])
        #     person=StudentInfoModel.objects.get(pk=line_list[2].split(' - ')[0])
        #     asset=PersonAssetInfoModel.objects.get(person=person)
        #     new=PeriodicPaymentModel(person_asset=asset,desc=line_list[16],company=company,month1=line_list[4])
        #     new.save()
        # elif line_list[0]==str(model_list[3]):#Transaction
        #     company=CompanyInfoModel.objects.get(pk=line_list[7])
        #     account=AccountInfoModel.objects.get(no=line_list[2].split(' - ')[0])
        #     new=TransactionInfoModel(account=account,type=line_list[3],amount=line_list[4],time=line_list[5],desc=line_list[6],company=company)
        #     new.save()
        # elif line_list[0]==str(model_list[5]):#event
        #     company=CompanyInfoModel.objects.get(pk=line_list[9])
        #     new=EventInfoModel(name=line_list[2],start_time=line_list[3],end_time=line_list[4],all_day=line_list[5],place=line_list[6],type=line_list[7],desc=line_list[8],company=company)
        #     new.save()
        # elif line_list[0]==str(model_list[12]):#personid
        #     company=CompanyInfoModel.objects.get(pk=line_list[18])
        #     new=PersonIDInfoModel(tcn=line_list[1],name=line_list[2],last_name=line_list[3],birth_day=line_list[4],birth_place=line_list[5],father=line_list[6],mother=line_list[7],nation=line_list[8],idcard_type=line_list[9],register_vilage=line_list[10],register_town=line_list[11],register_distinct=line_list[12],gender=line_list[13],nufus_cilt=line_list[14],nufus_ailesira=line_list[15],nufus_sirano=line_list[16],medeni_hali=line_list[17],company=company)
        #     new.save()
        # elif line_list[0]==str(model_list[14]):#student
        #     company=CompanyInfoModel.objects.get(pk=line_list[19])
        #     person=PersonIDInfoModel.objects.get(pk=line_list[2].split(' - ')[0])
        #     room=RoomInfoModel.objects.get(no=line_list[10],company=company)
        #     new=StudentInfoModel(id=line_list[1],tcn=person,phone=line_list[3],email=line_list[4],start_day=line_list[5],leave_day=None,city=line_list[7],town=line_list[8],address=line_list[9],room_id=room,type=line_list[11],school_name=line_list[12],education_year=line_list[13],blood_type=line_list[14],health_notes=line_list[15],special_notes=line_list[16],image_field=line_list[17],position=line_list[18],company=company)
        #     new.save()
        # elif line_list[0]==str(model_list[16]):#room
        #     company=CompanyInfoModel.objects.get(pk=line_list[7])
        #     new=RoomInfoModel(no=line_list[2],floor=line_list[3],people=line_list[4],type=line_list[5],desc=line_list[6],company=company)
        #     new.save()


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
