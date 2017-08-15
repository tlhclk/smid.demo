# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import FixtureInfoForm,RoomInfoForm
from .models import FixtureInfoModel,RoomInfoModel
from person_panel.models import StudentInfoModel
from user_panel.models import UserCompanyModel,CompanyInfoModel



def add_fixture(request):
    if request.user.has_perm('stock_panel.add_fixtureinfomodel'):
        company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id
        new_id=str(int(FixtureInfoModel.objects.all().order_by('-fixture_no')[0].fixture_no)+1)
        formfixture=FixtureInfoForm(initial={'fixture_no':new_id})
        if request.method=='POST':
            formfixture=FixtureInfoForm(request.POST,request.FILES)
            if formfixture.is_valid():
                formfixture.save()
                fixture=FixtureInfoModel.objects.last()
                fixture.company_id=CompanyInfoModel.objects.get(pk=company_id)
                fixture.save()
            return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
        room_list=RoomInfoModel.objects.filter(company_id=company_id)
        fixture_type_list=FixtureInfoModel.fixture_type_list
        return render(request,'stock_panel/add_fixture.html',{'formfixture':formfixture,'room_list':room_list,'fixture_type_list':fixture_type_list,'title':'Yeni Eşya Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_fixture(request):
    if request.user.has_perm('stock_panel.view_fixtureinfomodel'):
        fixture_list=FixtureInfoModel.objects.filter(company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id)
        return render(request,'stock_panel/table_fixture.html',{'fixture_list':fixture_list,'title':'Eşya Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def fixture_detail(request,fixture_no):
    if request.user.has_perm('stock_panel.view_fixtureinfomodel'):
        fixture=FixtureInfoModel.objects.get(pk=fixture_no)
        if fixture.company_id_id==UserCompanyModel.objects.get(pk=request.user.id).company_id:
            return render(request,'stock_panel/detail_fixture.html',{'fixture':fixture,'title':'Eşya Detayı'})
        else: return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_fixture(request,fixture_no):
    company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id
    if request.user.has_perm('stock_panel.change_fixtureinfomodel') and FixtureInfoModel.objects.get(pk=fixture_no).company_id_id == company_id:
        if request.method == "POST":
            formfixture=FixtureInfoForm(request.POST,request.FILES)
            if formfixture.is_valid():
                formfixture.save()
            return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
        formfixture = FixtureInfoForm(instance=FixtureInfoModel.objects.get(pk=fixture_no))
        room_list=RoomInfoModel.objects.filter(company_id=company_id)
        fixture_type_list=FixtureInfoModel.fixture_type_list
        return render(request,'stock_panel/add_fixture.html',{'formfixture':formfixture,'room_list':room_list,'fixture_type_list':fixture_type_list,'title':'Eşya Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.delete_fixtureinfomodel')  and FixtureInfoModel.objects.get(pk=fixture_no).company_id_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        FixtureInfoModel.objects.get(fixture_no=fixture_no).delete()
        return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')


def add_room(request):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id
        new_id=str(int(RoomInfoModel.objects.last().room_no)+1)
        formroom=RoomInfoForm(initial={'room_no':new_id})
        if request.method=='POST':
            formroom=RoomInfoForm(request.POST,request.FILES)
            if formroom.is_valid():
                formroom.save()
                room=RoomInfoModel.objects.last()
                room.company_id=CompanyInfoModel.objects.get(pk=company_id)
                room.save()
            return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
        room_people_list=RoomInfoModel.room_people_list
        room_type_list=RoomInfoModel.room_type_list
        return render(request,'stock_panel/add_room.html',{'formroom':formroom,'room_people_list':room_people_list,'room_type_list':room_type_list,'title':'Yeni Oda Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_room(request):
    if request.user.has_perm('stock_panel.view_roominfomodel'):
        room_list=RoomInfoModel.objects.filter(company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id)
        return render(request,'stock_panel/table_room.html',{'room_list':room_list,'title':'Oda Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def room_detail(request,room_id):
    if request.user.has_perm('stock_panel.view_roominfomodel'):
        room=RoomInfoModel.objects.get(pk=room_id)
        student_list=StudentInfoModel.objects.filter(room_id=room.room_id)
        bos_adet=int(room.room_people)-len(student_list)
        bos_list=['1' for i in range(bos_adet)]
        if room.company_id_id==UserCompanyModel.objects.get(pk=request.user.id).company_id:
            return render(request,'stock_panel/detail_room.html',{'room':room,'student_list':student_list,'bos_list':bos_list,'title':'Oda Detayı'})
        else: return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_room(request,room_id):
    company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id
    if request.user.has_perm('stock_panel.change_roominfomodel') and RoomInfoModel.objects.get(pk=room_id).company_id_id == company_id:
        formroom=RoomInfoForm(instance=RoomInfoModel.objects.get(pk=room_id))
        if request.method == "POST":
            formroom = RoomInfoForm(request.POST,instance=RoomInfoModel.objects.get(pk=room_id))
            if formroom.is_valid():
                formroom.save()
                return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
        room_people_list=RoomInfoModel.room_people_list
        room_type_list=RoomInfoModel.room_type_list
        return render(request,'stock_panel/add_room.html',{'formroom':formroom,'room_people_list':room_people_list,'room_type_list':room_type_list,'title':'Oda Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_room(request,room_id):
    if request.user.has_perm('stock_panel.delete_roominfomodel') and RoomInfoModel.objects.get(pk=room_id).company_id_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        FixtureInfoModel.objects.filter(room_id=room_id).delete()
        RoomInfoModel.objects.get(pk=room_id).delete()
        return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

