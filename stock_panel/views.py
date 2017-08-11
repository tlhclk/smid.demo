# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import FixtureInfoForm,RoomInfoForm
from .models import FixtureInfoModel,RoomInfoModel
from person_panel.models import StudentInfoModel



def add_fixture(request):
    if request.user.has_perm('stock_panel.add_fixtureinfomodel'):
        new_id=str(int(FixtureInfoModel.objects.all().order_by('-fixture_no')[0].fixture_no)+1)
        formfixture=FixtureInfoForm(initial={'fixture_no':new_id})
        if request.method=='POST':
            formfixture=FixtureInfoForm(request.POST,request.FILES)
            if formfixture.is_valid():
                formfixture.save()
            return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
        return render(request,'stock_panel/add_fixture.html',{'formfixture':formfixture,'model_info':FixtureInfoModel,'title':'Yeni Eşya Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_fixture(request):
    if request.user.has_perm('stock_panel.view_fixtureinfomodel'):
        fixture_list=FixtureInfoModel.objects.all()
        return render(request,'stock_panel/table_fixture.html',{'fixture_list':fixture_list,'title':'Eşya Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def fixture_detail(request,fixture_no):
    if request.user.has_perm('stock_panel.view_fixtureinfomodel'):
        fixture=FixtureInfoModel.objects.get(pk=fixture_no)
        return render(request,'stock_panel/detail_fixture.html',{'fixture':fixture,'title':'Eşya Detayı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.change_fixtureinfomodel'):
        if request.method == "POST":
            formfixture=FixtureInfoForm(request.POST,request.FILES)
            if formfixture.is_valid():
                formfixture.save()
            return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
        formfixture = FixtureInfoForm(instance=FixtureInfoModel.objects.get(pk=fixture_no))
        return render(request,'stock_panel/add_fixture.html',{'formfixture':formfixture,'model_info':FixtureInfoModel,'title':'Eşya Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.delete_fixtureinfomodel'):
        fixture=FixtureInfoModel.objects.get(fixture_no=fixture_no)
        fixture.delete()
        return redirect('http://127.0.0.1:8000/stock_panel/fixture_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')


def add_room(request):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        new_id=str(int(RoomInfoModel.objects.all().order_by('-room_no')[0].room_no)+1)
        formroom=RoomInfoForm(initial={'room_no':new_id})
        if request.method=='POST':
            formroom=RoomInfoForm(request.POST,request.FILES)
            if formroom.is_valid():
                formroom.save()
            return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
        return render(request,'stock_panel/add_room.html',{'formroom':formroom,'model_info':RoomInfoModel,'title':'Yeni Oda Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_room(request):
    if request.user.has_perm('stock_panel.view_roominfomodel'):
        room_list=RoomInfoModel.objects.all()
        return render(request,'stock_panel/table_room.html',{'room_list':room_list,'title':'Oda Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def room_detail(request,room_no):
    if request.user.has_perm('stock_panel.view_roominfomodel'):
        room=RoomInfoModel.objects.get(pk=room_no)
        student_list=StudentInfoModel.objects.filter(room_no=room.room_no)
        bos_adet=int(room.room_people)-len(student_list)
        bos_list=['1' for i in range(bos_adet)]
        return render(request,'stock_panel/detail_room.html',{'room':room,'student_list':student_list,'bos_list':bos_list,'title':'Oda Detayı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_room(request,room_no):
    if request.user.has_perm('stock_panel.change_roominfomodel'):
        formroom=RoomInfoForm(instance=RoomInfoModel.objects.get(pk=room_no))
        if request.method == "POST":
            formroom = RoomInfoForm(request.POST,instance=RoomInfoModel.objects.get(pk=room_no))
            if formroom.is_valid():
                formroom.save()
                return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
        return render(request,'stock_panel/add_room.html',{'formroom':formroom,'model_info':RoomInfoModel,'title':'Oda Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_room(request,room_no):
    if request.user.has_perm('stock_panel.delete_roominfomodel'):
        FixtureInfoModel.objects.filter(room_no=room_no).delete()
        RoomInfoModel.objects.get(room_no=room_no).delete()
        return redirect('http://127.0.0.1:8000/stock_panel/room_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

