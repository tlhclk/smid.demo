# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import FixtureInfoForm,RoomInfoForm
from .models import FixtureInfoModel,RoomInfoModel
from person_panel.models import StudentInfoModel



def add_fixture(request):
    if request.user.has_perm('stock_panel.add_fixtureinfomodel'):
        formfixture=FixtureInfoForm(user=request.user)
        if request.method=='POST':
            formfixture=FixtureInfoForm(user=request.user,POST=request.POST,FILES=request.FILES)
            if formfixture.is_valid():
                formfixture.save()
            return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
        return render(request,'stock_panel/add_fixture.html',{'formfixture':formfixture,'title':'Yeni Eşya Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_fixture(request,room_id):
    if request.user.has_perm('stock_panel.change_fixtureinfomodel'):
        fixture_list=FixtureInfoModel.objects.filter(company=request.user.company_id)
        if room_id: fixture_list=fixture_list.filter(room=room_id)
        return render(request,'stock_panel/table_fixture.html',{'fixture_list':fixture_list,'title':'Eşya Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def fixture_detail(request,fixture_no):
    if request.user.has_perm('stock_panel.change_fixtureinfomodel'):
        fixture=FixtureInfoModel.objects.get(pk=fixture_no)
        if fixture.company_id==request.user.company_id:
            return render(request,'stock_panel/detail_fixture.html',{'fixture':fixture,'title':'Eşya Detayı'})
        else: return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.add_fixtureinfomodel'):
        fixture=FixtureInfoModel.objects.get(pk=fixture_no,company=request.user.company_id)
        if request.method == "POST":
            formfixture=FixtureInfoForm(user=request.user,POST=request.POST,FILES=request.FILES,instance=fixture)
            if formfixture.is_valid():
                formfixture.save()
            return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
        formfixture = FixtureInfoForm(instance=fixture,user=request.user,initial={'image_field':fixture.image_field})
        return render(request,'stock_panel/add_fixture.html',{'formfixture':formfixture,'title':'Eşya Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.add_fixtureinfomodel'):
        FixtureInfoModel.objects.get(fixture_no=fixture_no,company=request.user.company_id).delete()
        return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')


def add_room(request):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        formroom=RoomInfoForm(user=request.user)
        if request.method=='POST':
            formroom=RoomInfoForm(user=request.user,POST=request.POST)
            if formroom.is_valid():
                formroom.save()
                return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
        return render(request,'stock_panel/add_room.html',{'formroom':formroom,'title':'Yurt Bilgileri'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_room(request):
    if request.user.has_perm('stock_panel.change_roominfomodel'):
        room_list=RoomInfoModel.objects.filter(company=request.user.company_id)
        return render(request,'stock_panel/table_room.html',{'room_list':room_list,'title':'Yurt Bilgileri'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def room_detail(request,room_id):
    if request.user.has_perm('stock_panel.change_roominfomodel'):
        room=RoomInfoModel.objects.get(pk=room_id)
        if room.company_id==request.user.company_id:
            return render(request,'stock_panel/detail_room.html',{'room':room,'title':'Yurt Bilgileri'})
        else: return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_room(request,room_id):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        room=RoomInfoModel.objects.get(pk=room_id,company=request.user.company_id)
        if request.method == "POST":
            formroom = RoomInfoForm(user=request.user,POST=request.POST,instance=room)
            if formroom.is_valid():
                formroom.save()
                return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
        formroom=RoomInfoForm(instance=room,user=request.user)
        return render(request,'stock_panel/add_room.html',{'formroom':formroom,'title':'Yurt Bilgileri'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_room(request,room_id):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        RoomInfoModel.objects.get(pk=room_id,company=request.user.company_id).delete()
        return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

