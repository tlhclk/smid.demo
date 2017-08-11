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
    return render(request,'report_panel/table_leave.html',{'leave_list':leave_list_now})

def contact_table(request):
    student_list=StudentInfoModel.objects.all()
    personal_list=PersonalInfoModel.objects.all()
    parent_list=ParentInfoModel.objects.all()
    return render(request, 'report_panel/table_contact.html', {'student_list':student_list, 'parent_list':parent_list, 'personal_list':personal_list})


def unpaid_rate(request):
    all_assets=PersonAssetInfoModel.objects.all()
    paid_asset_rate={}
    unpaid_asset_rate={}
    for asset in all_assets:
        all_transactions=TransactionInfoModel.objects.filter(transaction_desc__contains=asset.person_id_id)
        period = str((datetime.date.today() - asset.person_id.student_regday).days/30+1).split('.')[0]
        paid_asset_rate.setdefault(asset.asset_id, [])
        unpaid_asset_rate.setdefault(asset.asset_id, [])
        for transaction in all_transactions:
            rate = str((transaction.transaction_time.date() - asset.person_id.student_regday).days / 30 + 1).split('.')[0]
            if len(paid_asset_rate[asset.asset_id])!=0:
                paid_asset_rate[asset.asset_id].append(str(int(paid_asset_rate[asset.asset_id][-1])+1))
            else:
                paid_asset_rate[asset.asset_id].append('1')
        if len(paid_asset_rate[asset.asset_id])<int(period):
            for rate_time in range(1,int(period)+1):
                if str(rate_time) not in paid_asset_rate[asset.asset_id]:
                    unpaid_asset_rate[asset.asset_id].append(str(rate_time))
    return render(request,'report_panel/payment_info.html',{'paid_dict':paid_asset_rate,'unpaid_dict':unpaid_asset_rate})

def money_flow(request,account_no):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        transaction_list=TransactionInfoModel.objects.all()
        if account_no != '':
            transaction_list=TransactionInfoModel.objects.filter(account_no=account_no)
        all_money_list=[get_sum(transaction_list.filter(transaction_type=type_i[0])) for type_i in TransactionInfoModel.transaction_type_list]
        return render(request, 'report_panel/money_flow.html',{'title':'Aylık Para Akışı','monthly_sum':all_money_list})
    else: return redirect('http://www.dormoni.com/login/')

def get_sum(transaction_list):
    transaction_list = [transaction_list.filter(transaction_time__month=str(i)) for i in range(1, 13)]
    monthly_sum = [sum([float(x.transaction_amount) for x in transaction_list[i]]) for i in range(12)]
    return monthly_sum

def account_amount(request):
    account_list=AccountInfoModel.objects.all()
    month_list=['2017-1','2017-2','2017-3','2017-4','2017-5','2017-6','2017-7','2017-8','2017-9','2017-10','2017-11','2017-12']
    color_list=['rgba(255,0,0,0.6)','rgba(0,255,0,0.6)','rgba(0,0,255,0.6)','rgba(255,255,0,0.6)','rgba(255,0,255,0.6)',
                'rgba(0,255,255,0.6)','rgba(192,192,192,0.6)','rgba(255,127,0.6)','rgba(255,0,127,0.6)','rgba(127,255,0,0.6)']
    all_account_flow_list=[]
    check_box_list=[]
    for i,account in enumerate(account_list):
        i=i%10
        check_box_list.append((account.account_name,color_list[i]))
        account_process_dict={}
        for month in month_list:
            account_process_dict[month]=0.0
        transaction_list=TransactionInfoModel.objects.filter(account_no=account.account_no)
        for transaction in transaction_list:
            key=str(transaction.transaction_time.year)+'-'+str(transaction.transaction_time.month)
            if transaction.transaction_type == '1' or transaction.transaction_type == '7' or transaction.transaction_type == '8':
                account_process_dict[key]-=float(transaction.transaction_amount)
            else:
                account_process_dict[key] += float(transaction.transaction_amount)
        account_process_list=[]
        amount=account.account_amount
        for month in month_list:
            amount=float(amount)-float(account_process_dict[month])
            account_process_list.append(amount)
        all_account_flow_list.append({"label": account.account_name,
                                      "fillColor": color_list[i],
                                      "strokeColor": color_list[i],
                                      "pointColor": color_list[i],
                                      "pointStrokeColor": color_list[i],
                                      "pointHighlightFill": color_list[i],
                                      "pointHighlightStroke": color_list[i],
                                      "data": account_process_list})
    account_info=json.dumps(all_account_flow_list)
    asd=all_account_flow_list
    return render(request,'report_panel/account_graph.html',{'title':'Hesap Miktarı','account_info':account_info,'model_info':check_box_list})