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
            return redirect('https://dormoni.com/stock_panel/fixture_table/')
        return render(request,'stock_panel/add_fixture.html',{'formfixture':formfixture,'title':'Yeni Eşya Kaydı'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_fixture(request):
    if request.user.has_perm('stock_panel.add_fixtureinfomodel'):
        fixture_list=FixtureInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request,'stock_panel/table_fixture.html',{'fixture_list':fixture_list,'title':'Eşya Tablosu'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def fixture_detail(request,fixture_no):
    if request.user.has_perm('stock_panel.add_fixtureinfomodel'):
        fixture=FixtureInfoModel.objects.get(pk=fixture_no)
        if fixture.company_id_id==request.user.company_id_id:
            return render(request,'stock_panel/detail_fixture.html',{'fixture':fixture,'title':'Eşya Detayı'})
        else: return redirect('https://dormoni.com/stock_panel/fixture_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.change_fixtureinfomodel') and FixtureInfoModel.objects.get(pk=fixture_no).company_id_id == request.user.company_id_id:
        if request.method == "POST":
            formfixture=FixtureInfoForm(user=request.user,POST=request.POST,FILES=request.FILES,instance=FixtureInfoModel.objects.get(pk=fixture_no))
            if formfixture.is_valid():
                formfixture.save()
            return redirect('https://dormoni.com/stock_panel/fixture_table/')
        formfixture = FixtureInfoForm(instance=FixtureInfoModel.objects.get(pk=fixture_no),user=request.user,initial={'image_field':FixtureInfoModel.objects.get(pk=fixture_no).image_field})
        return render(request,'stock_panel/add_fixture.html',{'formfixture':formfixture,'title':'Eşya Düzenleme'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.delete_fixtureinfomodel')  and FixtureInfoModel.objects.get(pk=fixture_no).company_id_id == request.user.company_id_id:
        FixtureInfoModel.objects.get(fixture_no=fixture_no).delete()
        return redirect('https://dormoni.com/stock_panel/fixture_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')


def add_room(request):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        formroom=RoomInfoForm(user=request.user)
        if request.method=='POST':
            formroom=RoomInfoForm(user=request.user,POST=request.POST)
            print (formroom)
            if formroom.is_valid():
                formroom.save()
                return redirect('https://dormoni.com/stock_panel/room_table/')
        return render(request,'stock_panel/add_room.html',{'formroom':formroom,'title':'Yurt Bilgileri'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_room(request):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        room_list=RoomInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request,'stock_panel/table_room.html',{'room_list':room_list,'title':'Yurt Bilgileri'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def room_detail(request,room_id):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        room=RoomInfoModel.objects.get(pk=room_id)
        student_list=StudentInfoModel.objects.filter(room_id=room.id)
        bos_adet=int(room.people)-len(student_list)
        bos_list=['1' for i in range(bos_adet)]
        if room.company_id_id==request.user.company_id_id:
            return render(request,'stock_panel/detail_room.html',{'room':room,'title':'Yurt Bilgileri'})
        else: return redirect('https://dormoni.com/stock_panel/room_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_room(request,room_id):
    if request.user.has_perm('stock_panel.change_roominfomodel') and RoomInfoModel.objects.get(pk=room_id).company_id_id == request.user.company_id_id:
        formroom=RoomInfoForm(instance=RoomInfoModel.objects.get(pk=room_id),user=request.user)
        if request.method == "POST":
            formroom = RoomInfoForm(user=request.user,POST=request.POST,instance=RoomInfoModel.objects.get(pk=room_id))
            print(formroom)
            if formroom.is_valid():
                formroom.save()
                RoomInfoModel.objects.get(pk=room_id).delete()
                return redirect('https://dormoni.com/stock_panel/room_table/')
        return render(request,'stock_panel/add_room.html',{'formroom':formroom,'title':'Yurt Bilgileri'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_room(request,room_id):
    if request.user.has_perm('stock_panel.delete_roominfomodel') and RoomInfoModel.objects.get(pk=room_id).company_id_id == request.user.company_id_id:
        RoomInfoModel.objects.get(pk=room_id).delete()
        return redirect('https://dormoni.com/stock_panel/room_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

