from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FixtureInfoForm,RoomInfoForm,LiabilityInfoForm
from .models import FixtureInfoModel,RoomInfoModel,LiabilityInfoModel
from person_panel.models import StudentInfoModel


def option_menu(request):
    return render(request,'stock_panel/option_menu.html')

def add_fixture(request):
    if request.user.has_perm('stock_panel.add_fixtureinfomodel'):
        formfixture=FixtureInfoForm()
        if request.method=='POST':
            formfixture=FixtureInfoForm(request.POST,request.FILES)
            if formfixture.is_valid():
                formfixture.save()
            return redirect('../fixture_add')
        return render(request,'stock_panel/default_form.html',{'formfixture':formfixture})
    else: return HttpResponse('You have no Authoriztion')

def table_fixture(request):
    if request.user.has_perm('stock_panel.view_fixtureinfomodel'):
        fixture_list=FixtureInfoModel.objects.all()
        return render(request,'stock_panel/table_fixture.html',{'fixture_list':fixture_list})
    else: return HttpResponse('You have no Authoriztion')

def fixture_detail(request,fixture_no):
    if request.user.has_perm('stock_panel.view_fixtureinfomodel'):
        fixture=FixtureInfoModel.objects.get(pk=fixture_no)
        return render(request,'stock_panel/detail_fixture.html',{'fixture':fixture})
    else: return HttpResponse('You has no authorization to change fixture info')

def edit_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.change_fixtureinfomodel'):
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
        return render(request,'stock_panel/default_form.html',{'fixture':fixture})
    else: return HttpResponse('You has no authorization to change fixture info')

def delete_fixture(request,fixture_no):
    if request.user.has_perm('stock_panel.delete_fixtureinfomodel'):
        fixture=FixtureInfoModel.objects.get(fixture_no=fixture_no)
        fixture.delete()
        return redirect('../')
    else: return HttpResponse('You has no authorization to change fixture info')


def add_room(request):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        formroom=RoomInfoForm()
        if request.method=='POST':
            formroom=RoomInfoForm(request.POST,request.FILES)
            if formroom.is_valid():
                formroom.save()
            return redirect('../')
        return render(request,'stock_panel/default_form.html',{'formroom':formroom})
    else: return HttpResponse('You has no authorization to change fixture info')

def table_room(request):
    if request.user.has_perm('stock_panel.view_roominfomodel'):
        room_list=RoomInfoModel.objects.all()
        return render(request,'stock_panel/table_room.html',{'room_list':room_list})
    else: return HttpResponse('You has no authorization to change fixture info')

def room_detail(request,room_no):
    if request.user.has_perm('stock_panel.view_roominfomodel'):
        room=RoomInfoModel.objects.get(pk=room_no)
        student_list=StudentInfoModel.objects.filter(room_number=room.room_no)
        return render(request,'stock_panel/detail_room.html',{'room':room,'student_list':student_list})
    else: return HttpResponse('You has no authorization to change fixture info')

def edit_room(request,room_no):
    if request.user.has_perm('stock_panel.change_roominfomodel'):
        formroom=RoomInfoForm(instance=RoomInfoModel.objects.get(pk=room_no))
        if request.method == "POST":
            formroom = RoomInfoForm(request.POST,instance=RoomInfoModel.objects.get(pk=room_no))
            if formroom.is_valid():
                formroom.save()
                return redirect('../')
        return render(request,'stock_panel/default_form.html',{'form':formroom})
    else: return HttpResponse('You has no authorization to change room info')

def delete_room(request,room_no):
    if request.user.has_perm('stock_panel.delete_roominfomodel'):
        FixtureInfoModel.objects.filter(room_no=room_no).delete()
        RoomInfoModel.objects.get(room_no=room_no).delete()
        return redirect('../../room_table')
    else: return HttpResponse('You has no authorization to change room info')


def liability_add(request):
    if request.user.has_perm('stock_panel.add_liabilityinfomodel'):
        formliability=LiabilityInfoForm()
        if request.POST:
            formliability=LiabilityInfoForm(request.POST)
            if formliability.is_valid():
                formliability.save()
                return redirect('../')
        return render(request,'user_panel/default_form.html',{'form':formliability})
    else: return HttpResponse('You has no authorization to change room info')

def liability_detail(request,record_no):
    if request.user.has_perm('stock_panel.view_liabilityinfomodel'):
        liability=LiabilityInfoModel.objects.get(pk=record_no)
        return render(request,'stock_panel/detail_liability.html',{'liability':liability})
    else: return HttpResponse('You has no authorization to change room info')

def liability_table(request):
    if request.user.has_perm('stock_panel.view_liabilityinfomodel'):
        liability_list=LiabilityInfoModel.objects.all()
        return render(request,'stock_panel/table_liability.html',{'liability_list':liability_list})
    else: return HttpResponse('You has no authorization to change room info')

def liability_edit(request,record_no):
    if request.user.has_perm('stock_panel.change_liabilityinfomodel'):
        formliability=LiabilityInfoForm(instance=LiabilityInfoModel.objects.get(pk=record_no))
        if request.POST:
            formliability=LiabilityInfoForm(request.POST,instance=LiabilityInfoModel.objects.get(pk=record_no))
            if formliability.is_valid():
                formliability.save()
            return redirect('../')
        return render(request,'user_panel/default_form.html',{'form':formliability,'title':'Edit'})
    else: return HttpResponse('You has no authorization to change room info')

def liability_delete(request,record_no):
    if request.user.has_perm('stock_panel.delete_liabilityinfomodel'):
        LiabilityInfoModel.objects.get(pk=record_no).delete()
        return redirect('../')
    else: return HttpResponse('You has no authorization to change room info')
