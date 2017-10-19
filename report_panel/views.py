from django.shortcuts import render, redirect
from operation_panel.models import StudentLeaveModel,AttendanceInfoModel
from stock_panel.models import FixtureInfoModel,RoomInfoModel
from document_panel.models import LiabilityInfoModel,DocumentInfoModel
from person_panel.models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonIDInfoModel
from account_panel.models import AccountInfoModel,PersonAssetInfoModel,TransactionInfoModel,BillInfoModel
from user_panel.models import CompanyInfoModel,UserCompanyModel
from .forms import FilterAccountForm
import json
import datetime


def student_attendance(request,room_id,student_id):
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        if room_id and not student_id:
            student_list=StudentInfoModel.objects.filter(position=True,room_id=room_id,company_id=request.user.company_id_id)
            return render(request,'person_panel/table_student.html',{'student_list':student_list,'title':"%s No'lu Oda Yoklama Tablosu"% room_id}) #TODO: table_student.html dosyasında bi sorun var
        elif student_id and not room_id:
            return redirect('http://127.0.0.1:8000/person_panel/student/%s'%student_id)
        else:
            student_list=StudentInfoModel.objects.filter(position=True,company_id=request.user.company_id_id)
            return render(request,'person_panel/table_student.html',{'student_list':student_list,'title':'Yoklama Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def dorm_capacity(request,room_id):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        if room_id!='':
            room=RoomInfoModel.objects.get(pk=room_id)
            if room.company_id_id==request.user.company_id_id:
                student_number=len(StudentInfoModel.objects.filter(room_id=room_id,company_id=request.user.company_id_id))
                return render(request,'report_panel/graph_capacity.html',{'room':room,'student_number':student_number,'title':'Kontenjan Grafiği'})
        else:
            all_rooms=RoomInfoModel.objects.filter(company_id=request.user.company_id_id)
            student_number=len(StudentInfoModel.objects.filter(company_id=request.user.company_id_id))
            quota_number=sum([int(room.room_people) for room in all_rooms])-student_number
            return render(request,'report_panel/graph_capacity.html',{'student_number':student_number,'quota_number':quota_number,'title':'Kontenjan Grafiği'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def room_plan(request):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        room_list=RoomInfoModel.objects.filter(company_id=request.user.company_id_id).order_by('no')
        room_list_four=[]
        for i in range(0,len(room_list),4):
            temp_list=[]
            for k in range(4):
                try:
                    temp_list.append(room_list[i+k])
                except IndexError:
                    pass
            room_list_four.append(temp_list)
        student_list=StudentInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request, 'report_panel/room_plan.html', {'room_list_four': room_list_four,'student_list':student_list,'title':'Oda Planı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def contact_table(request):
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        student_list=StudentInfoModel.objects.filter(company_id=request.user.company_id_id)
        personal_list=PersonalInfoModel.objects.filter(company_id=request.user.company_id_id)
        parent_list=ParentInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request, 'report_panel/table_contact.html', {'title':'Rehber Tablosu','student_list':student_list, 'parent_list':parent_list, 'personal_list':personal_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def unpaid_rate(request):# TODO: tekrar gözden geçirilecek yanlış sonuç veriyor
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        all_assets=PersonAssetInfoModel.objects.filter(company_id=request.user.company_id_id)
        paid_asset_rate={}
        unpaid_asset_rate={}
        for asset in all_assets:
            all_transactions=TransactionInfoModel.objects.filter(desc__contains=asset.person_id,company_id=request.user.company_id_id)
            period = str((datetime.date.today() - asset.person.start_day).days/30+1).split('.')[0]
            paid_asset_rate.setdefault(asset.id, [])
            unpaid_asset_rate.setdefault(asset.id, [])
            for transaction in all_transactions:
                rate = str((transaction.time.date() - asset.person.start_day).days / 30 + 1).split('.')[0]
                if len(paid_asset_rate[asset.id])!=0:
                    paid_asset_rate[asset.id].append(str(int(paid_asset_rate[asset.id][-1])+1))
                else:
                    paid_asset_rate[asset.id].append('1')
            if len(paid_asset_rate[asset.id])<int(period):
                for rate_time in range(1,int(period)+1):
                    if str(rate_time) not in paid_asset_rate[asset.id]:
                        unpaid_asset_rate[asset.id].append(str(rate_time))
        return render(request,'report_panel/payment_info.html',{'paid_dict':paid_asset_rate,'unpaid_dict':unpaid_asset_rate})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def money_flow(request,account_no):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        transaction_list=TransactionInfoModel.objects.filter(company_id=request.user.company_id_id)
        if account_no != '':
            transaction_list=TransactionInfoModel.objects.filter(account_no=account_no,company_id=request.user.company_id_id)
        all_money_list=[get_sum(transaction_list.filter(type=type_i[0])) for type_i in TransactionInfoModel.transaction_type_list]
        return render(request, 'report_panel/money_flow.html',{'title':'Aylık Para Akışı','monthly_sum':all_money_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def get_sum(transaction_list):
    transaction_list = [transaction_list.filter(time__month=str(i)) for i in range(1, 13)]
    monthly_sum = [sum([float(x.amount) for x in transaction_list[i]]) for i in range(12)]
    return monthly_sum

def account_amount(request):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        account_list=AccountInfoModel.objects.filter(company_id=request.user.company_id_id)
        month_list=['2017-1','2017-2','2017-3','2017-4','2017-5','2017-6','2017-7','2017-8','2017-9','2017-10','2017-11','2017-12']
        color_list=['rgba(255,0,0,0.6)','rgba(0,255,0,0.6)','rgba(0,0,255,0.6)','rgba(255,255,0,0.6)','rgba(255,0,255,0.6)',
                    'rgba(0,255,255,0.6)','rgba(192,192,192,0.6)','rgba(255,127,0.6)','rgba(255,0,127,0.6)','rgba(127,255,0,0.6)']
        all_account_flow_list=[]
        check_box_list=[]
        for i,account in enumerate(account_list):
            i=i%10
            check_box_list.append((account.name,color_list[i]))
            account_process_dict={}
            for month in month_list:
                account_process_dict[month]=0.0
            transaction_list=TransactionInfoModel.objects.filter(account_no=account.no,company_id=request.user.company_id_id)
            for transaction in transaction_list:
                key=str(transaction.time.year)+'-'+str(transaction.time.month)
                if transaction.type == '1' or transaction.type == '7' or transaction.type == '8':
                    account_process_dict[key]-=float(transaction.amount)
                else:
                    account_process_dict[key] += float(transaction.amount)
            account_process_list=[]
            amount=account.amount
            for month in month_list:
                amount=float(amount)-float(account_process_dict[month])
                account_process_list.append(amount)
            all_account_flow_list.append({"label": account.name,
                                          "fillColor": color_list[i],
                                          "strokeColor": color_list[i],
                                          "pointColor": color_list[i],
                                          "pointStrokeColor": color_list[i],
                                          "pointHighlightFill": color_list[i],
                                          "pointHighlightStroke": color_list[i],
                                          "data": account_process_list})
        account_info=json.dumps(all_account_flow_list)
        return render(request,'report_panel/account_graph.html',{'title':'Hesap Miktarı','account_info':account_info,'model_info':check_box_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')

def monthly_flow(request,month='07'):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        color_list = ["rgba(255,0,0,0.6)", "rgba(0,255,0,0.6)", "rgba(0,0,255,0.6)", "rgba(255,255,0,0.6)","rgba(255,0,255,0.6)","rgba(0,255,255,0.6)", "rgba(192,192,192,0.6)", "rgba(255,127,0.6)", "rgba(255,0,127,0.6)","rgba(127,255,0,0.6)"]
        transaction_list=TransactionInfoModel.objects.filter(time__month=month,company_id=request.user.company_id_id)
        transaction_json=[]
        transaction_data=[(color_list[int(index)-1],tra_type,index) for index,tra_type in TransactionInfoModel.transaction_type_list]
        for index,tra_type in enumerate(TransactionInfoModel.transaction_type_list):
            transaction_json.append({"value":sum([float(transaction.amount) for transaction in transaction_list.filter(type=tra_type[0])]),"color":color_list[index],"highlight":color_list[index],"label":tra_type[1]})
        transaction_json=json.dumps(transaction_json)
        return render(request,'report_panel/monthly_flow.html',{'title':'Aylık Akış','transaction_json':transaction_json,'transaction_data':transaction_data})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')


def filter_form(request):#TODO: sonuç gösterilmiyor tekrar düzenlenecek
    color_list = ["rgba(255,0,0,0.6)", "rgba(0,255,0,0.6)", "rgba(0,0,255,0.6)", "rgba(255,255,0,0.6)",
                  "rgba(255,0,255,0.6)", "rgba(0,255,255,0.6)", "rgba(192,192,192,0.6)", "rgba(255,127,0.6)",
                  "rgba(255,0,127,0.6)", "rgba(127,255,0,0.6)"]
    formfilter=FilterAccountForm(request.POST,None)
    transation_list=TransactionInfoModel.objects.filter(company_id=request.user.company_id_id)
    if formfilter.is_valid():
        account_no=formfilter['account_no'].value()
        year=formfilter['year'].value()
        month=formfilter['month'].value()
        day=formfilter['day'].value()
        transation_type=formfilter['transaction_type'].value()
        student_id=formfilter['student_id'].value()
        deposito=formfilter['deposito'].value()
        if account_no:
            transation_list=transation_list.filter(account_no=account_no)
        if year:
            transation_list =transation_list.filter(time__year=year)
        if month:
            transation_list =transation_list.filter(time__month=month)
        if day:
            transation_list =transation_list.filter(time__day=day)
        if transation_type:
            transation_list =transation_list.filter(type=transation_type)
        if student_id:
            transation_list =transation_list.filter(desc__contains=student_id)
        if deposito:
            transation_list =transation_list.filter(desc__contains='deposito')
        json_list=[]
        data=[]
        for index, amount in enumerate(transation_list):
            data.append(float(amount.amount))
        i=0
        json_list=[{"label":data,
                  "fillColor": color_list[i],
                  "strokeColor": color_list[i],
                  "pointColor": color_list[i],
                  "pointStrokeColor": color_list[i],
                  "pointHighlightFill": color_list[i],
                  "pointHighlightStroke": color_list[i],
                    'data':data}]
        return render(request, 'report_panel/form_filter_account.html', {'form': formfilter, 'transaction_list': transation_list,'json_list':json.dumps(json_list)})
    return render(request,'report_panel/form_filter_account.html',{'form':formfilter, 'transaction_list': transation_list})
    # aylık işlem türü miktarı
    #transaction_sum0=sum([float(transaction.transaction_amount) for transaction in TransactionInfoModel.objects.filter(transaction_time__month=month,transaction_type=tra_type)])
    # aylık hesap türü miktarı
    #transaction_sum1=sum([float(transaction.transaction_amount) for transaction in TransactionInfoModel.objects.filter(transaction_time__month=month,account_no=account)])
    # aylık hesap ve işlem türü miktarı
    #transaction_sum2=sum([float(transaction.transaction_amount) for transaction in TransactionInfoModel.objects.filter(transaction_time__month=month,account_no=account,transaction_type=tra_type)])
    # deposito miktarı
    #transaction_sum3=sum([float(transaction.transaction_amount) for transaction in TransactionInfoModel.objects.filter(transaction_time__month=month,)])

