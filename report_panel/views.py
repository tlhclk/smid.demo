from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from operation_panel.models import StudentLeaveModel
from stock_panel.models import FixtureInfoModel,RoomInfoModel
from document_panel.models import LiabilityInfoModel
from person_panel.models import StudentInfoModel,ParentInfoModel,PersonalInfoModel
import datetime

def options_menu(request):
    room_list=RoomInfoModel.objects.all().order_by('room_no')
    student_list=StudentInfoModel.objects.all()
    return render(request,'report_panel/option_menu.html',{'room_list':room_list,'student_list':student_list})

def student_attendance(request,room_no,student_id):
    if room_no and not student_id:
        report_type='Students in Room %s: ' %room_no
        current=StudentInfoModel.objects.filter(student_position=True,room_number=room_no)
        all=StudentInfoModel.objects.filter(room_number=room_no)
        return render(request,'report_panel/report_attendance.html',{'report_type':report_type,'current':current,'all':all})
    elif student_id and not room_no:
        report_type='Student numbered: %s' % student_id
        stu=StudentInfoModel.objects.get(pk=student_id)
        return render(request,'report_panel/report_attendance.html',{'report_type':report_type,'stu':stu})
    else:
        report_type='All students in Dorm'
        current=StudentInfoModel.objects.filter(student_position=True)
        all=StudentInfoModel.objects.all()
        return render(request,'report_panel/report_attendance.html',{'report_type':report_type,'current':current,'all':all})

def dorm_capacity(request,room_no):
    if room_no!='':
        report_type='Room No %s Capacity Report' % room_no
        room_capacity=RoomInfoModel.objects.get(pk=room_no).room_people
        student_list=StudentInfoModel.objects.filter(room_number=room_no)
        return render(request,'report_panel/report_capacity.html',{'report_type':report_type,'student_list':student_list,'room_capacity':room_capacity})
    else:
        report_type='All Dorm Capacity'
        all_rooms=RoomInfoModel.objects.all()
        all_capacity=sum([int(room.room_people) for room in all_rooms])
        full_part=len(StudentInfoModel.objects.all())
        return render(request,'report_panel/report_capacity.html',{'report_type':report_type,'all_capacity':all_capacity,'full_part':full_part})

def room_plan(request):
    room_list=RoomInfoModel.objects.all()
    student_list=StudentInfoModel.objects.all()
    return render(request, 'report_panel/room_plan.html', {'room_list': room_list,'student_list':student_list})

def leave_permission_table(request):
    leave_list=StudentLeaveModel.objects.all()
    leave_list_now=[]
    for leave_record in leave_list:
        print (leave_record.leave_start,datetime.date.today(),leave_record.leave_end)
        if datetime.datetime.strptime(str(leave_record.leave_start),"%Y-%m-%d")<=datetime.datetime.strptime(str(datetime.date.today()),"%Y-%m-%d")<=datetime.datetime.strptime(str(leave_record.leave_end),"%Y-%m-%d"):
            leave_list_now.append(leave_record)
    print (leave_list_now)
    return render(request,'report_panel/leave_table.html',{'leave_list':leave_list_now})

def contact_table(request):
    student_list=StudentInfoModel.objects.all()
    personal_list=PersonalInfoModel.objects.all()
    parent_list=ParentInfoModel.objects.all()
    return render(request, 'report_panel/table_contact.html', {'student_list':student_list, 'parent_list':parent_list, 'personal_list':personal_list})

def calendar(request):
    student_list=[student for student in StudentInfoModel.objects.all()]
    for student in student_list:
        print (student.student_regday.day)
    return render(request,'smidDemo/pages/examples/calendar.html',{'student_list':student_list})


