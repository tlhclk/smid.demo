from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from operation_panel.models import StudentLeaveModel,AttendanceInfoModel
from stock_panel.models import FixtureInfoModel,RoomInfoModel
from document_panel.models import LiabilityInfoModel,DocumentInfoModel
from person_panel.models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonIDInfoModel
from account_panel.models import AccountInfoModel,PersonAssetInfoModel,TransactionInfoModel,BillInfoModel
import json

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
        room_capacity=RoomInfoModel.objects.get(pk=room_no).room_people
        student_list=StudentInfoModel.objects.filter(room_number=room_no)
        return render(request,'report_panel/report_capacity.html',{'student_list':student_list,'room_capacity':room_capacity})
    else:
        all_rooms=RoomInfoModel.objects.all()
        quota_number=sum([int(room.room_people) for room in all_rooms])
        student_number=len(StudentInfoModel.objects.all())
        return render(request,'report_panel/report_capacity.html',{'student_number':student_number,'quota_number':quota_number,'title':'Kontenjan Grafiği'})

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

def unpaid_rate(request):
    all_assets=PersonAssetInfoModel.objects.all()
    paid_asset_rate={}
    unpaid_asset_rate={}
    for asset in all_assets:
        all_transactions=TransactionInfoModel.objects.filter(transaction_desc__contains=asset.person_id_id)
        period = str((timezone.now() - asset.person_id.student_regday).days/30+1).split('.')[0]
        paid_asset_rate.setdefault(asset.asset_id, [])
        unpaid_asset_rate.setdefault(asset.asset_id, [])
        for transaction in all_transactions:
            rate = str((transaction.transaction_time - asset.person_id.student_regday).days / 30 + 1).split('.')[0]
            if len(paid_asset_rate[asset.asset_id])!=0:
                paid_asset_rate[asset.asset_id].append(str(int(paid_asset_rate[asset.asset_id][-1])+1))
            else:
                paid_asset_rate[asset.asset_id].append('1')
        if len(paid_asset_rate[asset.asset_id])<int(period):
            for rate_time in range(1,int(period)+1):
                if str(rate_time) not in paid_asset_rate[asset.asset_id]:
                    unpaid_asset_rate[asset.asset_id].append(str(rate_time))
    print (paid_asset_rate)
    print (unpaid_asset_rate)
    return render(request,'report_panel/payment_info.html',{'paid_dict':paid_asset_rate,'unpaid_dict':unpaid_asset_rate})


def birthday_calendar(request,filter_time='07'):
    student_list=PersonIDInfoModel.objects.all()
    personal_list=PersonalInfoModel.objects.all()
    json_dict={}
    birthday_list=[]
    for student in student_list:
        if student.s_birthday:
            print (student.full_name())
            birthday_list.append((student.full_name(),student.s_birthday))
            json_dict.setdefault(student.full_name(),{'month':student.s_birthday.month,'day':student.s_birthday.day})

    for personal in personal_list:
        if personal.personal_birthday:
            print (personal.full_name())
            birthday_list.append((personal.full_name(),personal.personal_birthday))
            json_dict.setdefault(personal.full_name(),{'month': personal.personal_birthday.month, 'day': personal.personal_birthday.day})

    birthday_json=open('templates/smidDemo/birthday_list.json','w+',encoding='utf8')
    birthday_json.write(json.dumps(json_dict,indent=4,sort_keys=True,separators=(',', ': '), ensure_ascii=False,))
    birthday_json.close()
    return render(request,'report_panel/denem_birthday.html',{'birthday_list':birthday_list,'personal_list':personal_list,'student_list':student_list})