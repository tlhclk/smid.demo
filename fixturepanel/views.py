from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import FixtureInfoForm,RoomInfoForm
from .models import FixtureInfoModel,RoomInfoModel
from studentpanel.models import StudentInfoModel

def options_menu(request):
    return render(request,'fixture_panel/options_menu.html')

def add_fixture(request):
    formfixture=FixtureInfoForm()
    if request.method=='POST':
        formfixture=FixtureInfoForm(request.POST,request.FILES)
        if formfixture.is_valid():
            formfixture.save()
        return redirect('../fixture_add')
    return render(request,'fixture_panel/fixture_add.html',{'formfixture':formfixture})

def table_fixture(request):
    fixture_list=FixtureInfoModel.objects.all()
    return render(request,'fixture_panel/fixture_table.html',{'fixture_list':fixture_list})

def fixture_detail(request,fixture_no):
    fixture=FixtureInfoModel.objects.get(pk=fixture_no)
    return render(request,'fixture_panel/fixture_detail.html',{'fixture':fixture})

def edit_fixture(request,fixture_no):
    if request.user.has_perm('fixturepanel.change_fixtureinfomodel'):
        if request.method == "POST":
            fixture = FixtureInfoModel.objects.get(pk=fixture_no)
            fixture.fixture_no=request.POST['fixture_no']
            fixture.room_no=RoomInfoModel.objects.get(pk=request.POST['room_no'])
            fixture.fixture_type=request.POST['fixture_type']
            fixture.fixture_notes=request.POST['fixture_notes']
            fixture.fixture_image=request.POST['fixture_image']
            fixture.save()
            return redirect('../../')
        fixture = FixtureInfoModel.objects.get(pk=fixture_no)
        return render(request,'fixture_panel/edit_fixture.html',{'fixture':fixture})
    else: return HttpResponse('You has no authorization to change fixture info')

def delete_fixture(request,fixture_no):
    fixture=FixtureInfoModel.objects.get(fixture_no=fixture_no)
    fixture.delete()
    return redirect('../../fixture_table')


def add_room(request):
    formroom=RoomInfoForm()
    if request.method=='POST':
        formroom=RoomInfoForm(request.POST,request.FILES)
        if formroom.is_valid():
            formroom.save()
        return redirect('../room_add')
    return render(request,'fixture_panel/room_add.html',{'formroom':formroom})

def table_room(request):
    room_list=RoomInfoModel.objects.all()

    return render(request,'fixture_panel/room_table.html',{'room_list':room_list})

def room_detail(request,room_no):
    room=RoomInfoModel.objects.get(pk=room_no)
    room_people=RoomInfoModel.room_people_list[int(room.room_people)-1]
    room_type=RoomInfoModel.room_type_list[int(room.room_type)-1]
    student_list=StudentInfoModel.objects.filter(room_number=room.room_no)
    return render(request,'fixture_panel/room_detail.html',{'room':room,'room_people':room_people,'room_type':room_type,'student_list':student_list})

def edit_room(request,room_no):
    if request.user.has_perm('roompanel.change_roominfomodel'):
        if request.method == "POST":
            room = RoomInfoModel.objects.get(pk=room_no)
            room.room_no=request.POST['room_no']
            room.room_floor=request.POST['room_floor']
            room.room_people=request.POST['room_people']
            room.room_type=request.POST['room_type']
            room.room_desc=request.POST['room_desc']
            room.room_image=request.POST['room_image']
            room.save()
            return redirect('../../')
        room = RoomInfoModel.objects.get(pk=room_no)
        return render(request,'fixture_panel/edit_room.html',{'room':room})
    else: return HttpResponse('You has no authorization to change room info')

def delete_room(request,room_no):
    room=RoomInfoModel.objects.get(room_no=room_no)
    fixture_list=FixtureInfoModel.objects.filter(room_no=room_no)
    for fixture in fixture_list:
        fixture.room_no='Not Assigned'
        fixture.save()
    room.delete()
    return redirect('../../room_table')


