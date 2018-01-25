from django.shortcuts import render, redirect
from stock_panel.models import RoomInfoModel
from person_panel.models import StudentInfoModel,ParentInfoModel,PersonalInfoModel
from account_panel.models import AccountInfoModel,PersonAssetInfoModel,TransactionInfoModel
from .forms import FilterAccountForm
import json
import datetime,re,pytz


def student_attendance(request,room_id,student_id):
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        if room_id and not student_id:
            student_list=StudentInfoModel.objects.filter(position=True,room_id=room_id,company=request.user.company_id)
            return render(request,'person_panel/table_student.html',{'student_list':student_list,'title':"%s No'lu Oda Yoklama Tablosu"% room_id}) #TODO: table_student.html dosyasında bi sorun var
        elif student_id and not room_id:
            return redirect('http://127.0.0.1:8000/person_panel/student/%s'%student_id)
        else:
            student_list=StudentInfoModel.objects.filter(position=True,company=request.user.company_id)
            return render(request,'person_panel/table_student.html',{'student_list':student_list,'title':'Yoklama Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')


def dorm_capacity(request,room_id):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        if room_id!='':
            room=RoomInfoModel.objects.get(pk=room_id)
            if room.company_id==request.user.company_id:
                student_number=len(room.people_list())
                quota_number=int(room.people)-student_number
                return render(request,'report_panel/graph_capacity.html',{'room':room,'student_number':student_number,'quota_number':quota_number,'title':'Kontenjan Grafiği'})
        else:
            all_rooms=RoomInfoModel.objects.filter(company=request.user.company_id)
            student_number=len(StudentInfoModel.objects.filter(company=request.user.company_id))
            quota_number=sum([int(room.people) for room in all_rooms])-student_number
            return render(request,'report_panel/graph_capacity.html',{'student_number':student_number,'quota_number':quota_number,'title':'Yurt Bilgileri'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')


def room_plan(request):
    if request.user.has_perm('stock_panel.add_roominfomodel'):
        room_list=RoomInfoModel.objects.filter(company=request.user.company_id).order_by('no')
        room_floor_list=[('0','Kat Seçiniz')]
        for room in room_list:
            if (room.floor,room.floor) not in room_floor_list:
                room_floor_list.append((room.floor,room.floor))
        return render(request, 'report_panel/room_plan.html', {'room_list': room_list,'title':'Yurt Bilgileri','room_floor':room_floor_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')


def contact_table(request):
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        student_list=StudentInfoModel.objects.filter(company=request.user.company_id)
        personal_list=PersonalInfoModel.objects.filter(company=request.user.company_id)
        parent_list=ParentInfoModel.objects.filter(company=request.user.company_id)
        return render(request, 'report_panel/table_contact.html', {'title':'Rehber Tablosu','student_list':student_list, 'parent_list':parent_list, 'personal_list':personal_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')


def unpaid_rate(request):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        all_assets=PersonAssetInfoModel.objects.filter(company=request.user.company_id)
        all_transactions=TransactionInfoModel.objects.filter(type='7',company=request.user.company_id)
        paid_asset_rate={}
        unpaid_asset_rate={}
        for asset in all_assets:
            period = (datetime.date.today().month - asset.person.start_day.month)
            if int(asset.period)<period:
                period=int(asset.period)
            paid_asset_rate.setdefault(asset.id, ['' for n in range (period)])
        for transaction in all_transactions:
            id = re.search('[0-9]+', transaction.desc).group()
            if StudentInfoModel.objects.get(pk=id):
                asset = PersonAssetInfoModel.objects.filter(person=id)[0]
                rate = (transaction.time.month - asset.person.start_day.month)
                if paid_asset_rate[asset.id][rate]=='':
                    paid_asset_rate[asset.id][rate]=transaction.amount
                else:
                    for r in range(len(paid_asset_rate[asset.id])):
                        if paid_asset_rate[asset.id][r]=='':
                            paid_asset_rate[asset.id][r]=transaction.amount
                            break
        if 1==1:
            payer_list=[]
            for id,rate in paid_asset_rate.items():
                if '' in rate:
                    payer_list.append(PersonAssetInfoModel.objects.get(pk=id).person.id)

        return render(request,'report_panel/payment_info.html',{'paid_dict':paid_asset_rate,'title':'Ödeme Bilgileri'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login')


def get_sum(transaction_list):
    transaction_list = [transaction_list.filter(time__month=str(i)) for i in range(1, 13)]
    monthly_sum = [sum([float(x.amount) for x in transaction_list[i]]) for i in range(12)]
    return monthly_sum


def account_graphs(request,account_no):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        ##money_flow
        transaction_list=TransactionInfoModel.objects.filter(company=request.user.company_id)
        if account_no != '':
            transaction_list=TransactionInfoModel.objects.filter(account_no=account_no,company=request.user.company_id)
        all_money_list=[]
        for type_i in TransactionInfoModel.transaction_type_list:
            all_money_list.append([type_i[1],get_sum(transaction_list.filter(type=type_i[0]))])
        monthly_sum=json.dumps(all_money_list)
        ##account_amount
        account_list=AccountInfoModel.objects.filter(company=request.user.company_id)
        transaction_list=TransactionInfoModel.objects.filter(company=request.user.company_id)
        aa_dict={}
        for account in account_list:
            aa_dict.setdefault(account,[0.0 for n in range(12)])
            for trans in transaction_list.filter(account=account.no).order_by('-time'):
                if trans.type=='1' or trans.type=='7':
                    if aa_dict[account][trans.time.month]==0.0:
                        aa_dict[account][trans.time.month]=float(trans.amount)
                    else:
                        aa_dict[account][trans.time.month]+=float(trans.amount)
                else:
                    if aa_dict[account][trans.time.month]==0.0:
                        aa_dict[account][trans.time.month]=float(trans.amount)
                    else:
                        aa_dict[account][trans.time.month]-=float(trans.amount)
        at_dit={}
        for account in account_list:
            amount_list=aa_dict[account]
            at_dit.setdefault(account.name,[float(account.amount)])
            for month in amount_list:
                at_dit[account.name].append(at_dit[account.name][-1]+month)
        account_info=json.dumps(list(at_dit.items()))
        ##monthly_flow
        return render(request,'report_panel/account_graph.html',{'title':'Muhasebe','account_info':account_info,'monthly_sum':monthly_sum},)
    else: return redirect('http://127.0.0.1:8000/user_panel/login')


def monthly_flow(request,month):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        if not month:
            month=datetime.datetime.today().month
        transaction_list=TransactionInfoModel.objects.filter(time__month=month,company=request.user.company_id)
        transaction_json=[]
        for tra_type in TransactionInfoModel.transaction_type_list:
            transaction_json.append([tra_type[1],sum([float(transaction.amount) for transaction in transaction_list.filter(type=tra_type[0])])])
        transaction_json=json.dumps(transaction_json)
        return render(request,'report_panel/monthly_flow.html',{'title':'Aylık Akış','transaction_json':transaction_json})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')


def salary_table(request):
    all_personal=PersonalInfoModel.objects.filter(company=request.user.company_id)
    all_transactions=TransactionInfoModel.objects.filter(company=request.user.company_id)
    yearly_salary_dict={}
    for person in all_personal:
        yearly_salary_dict.setdefault(person,['' for a in range(12)])
        transaction_list=all_transactions.filter(desc__contains=person.id,type='8')
        now=datetime.datetime.now()
        for index,tra in enumerate(transaction_list):
            now=now.replace(tzinfo=pytz.UTC)
            dif=now-tra.time
            if dif<datetime.timedelta(days=365.0,):
                yearly_salary_dict[person][-dif.days//30]=tra.amount
            else:
                break
    return render(request,'report_panel/salary_table.html',{'title':'Maaş Tablosu','yearly_salary_dict':yearly_salary_dict})


def filter_form(request):#TODO:tekrar düzenlenecek
    color_list = ["rgba(255,0,0,0.6)", "rgba(0,255,0,0.6)", "rgba(0,0,255,0.6)", "rgba(255,255,0,0.6)",
                  "rgba(255,0,255,0.6)", "rgba(0,255,255,0.6)", "rgba(192,192,192,0.6)", "rgba(255,127,0.6)",
                  "rgba(255,0,127,0.6)", "rgba(127,255,0,0.6)"]
    formfilter=FilterAccountForm(request.POST,None)
    transation_list=TransactionInfoModel.objects.filter(company=request.user.company_id)
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
