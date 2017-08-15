# -*- coding: utf-8 -*-
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.core import mail
from .forms import StudentInfoForm,ParentInfoForm,PersonalInfoForm,PersonIDInfoForm
from .models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonIDInfoModel
from user_panel.models import UserCompanyModel,CompanyInfoModel
from stock_panel.models import RoomInfoModel


def add_student(request):
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id
        new_id=str(int(StudentInfoModel.objects.all().order_by('-id')[0].id)+1)
        formstudent = StudentInfoForm(initial={'id':new_id})
        if request.method == "POST":
            formstudent = StudentInfoForm(request.POST, request.FILES)
            if formstudent.is_valid():
                id=formstudent.cleaned_data.get('id')
                student_tcn = formstudent.cleaned_data.get('student_tcn')
                first_name= student_tcn.s_name
                last_name = student_tcn.s_lastname
                email = formstudent.cleaned_data.get('e_mail')
                new_user_add(first_name, last_name, email,id,'1',company_id)
                formstudent.save()
                profile_pic_config(StudentInfoModel.objects.get(pk=id))
                student=StudentInfoModel.objects.last()
                student.company_id=CompanyInfoModel.objects.get(pk=company_id)
                student.save()
            return redirect('http://127.0.0.1:8000/account_panel/asset_add/')
        tcn_list=PersonIDInfoModel.objects.filter(company_id=company_id)
        city_list=StudentInfoModel().city_list()
        room_list=RoomInfoModel.objects.filter(company_id=company_id)
        student_type_list=StudentInfoModel.student_type_list
        year_list=StudentInfoModel.year_list
        blood_type_list=StudentInfoModel.blood_type_list
        return render(request, 'person_panel/add_student.html', {'form': formstudent,'tcn_list':tcn_list,'city_list':city_list,'room_list':room_list,'student_type_list':student_type_list,'year_list':year_list,'blood_type_list':blood_type_list,'title':'Yeni Öğrenci Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_student(request,student_id):
    if request.user.has_perm('person_panel.view_studentinfomodel'):
        student = StudentInfoModel.objects.get(pk=student_id)
        parent = ParentInfoModel.objects.filter(student_id=student_id)[0]
        if student.company_id_id==UserCompanyModel.objects.get(pk=request.user.id).company_id:
            return render(request, 'person_panel/detail_student.html', {'student': student,'parent':parent,'title':'Öğrenci Detayı'})
        else: return redirect('http://127.0.0.1:8000/person_panel/student_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_student(request):
    if request.user.has_perm('person_panel.view_studentinfomodel'):
        student_list=StudentInfoModel.objects.filter(company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id)
        return  render(request, 'person_panel/table_student.html',{'student_list':student_list, 'title': 'Öğrenci Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_student(request,student_id):
    company_id = UserCompanyModel.objects.get(pk=request.user.id).company_id
    if request.user.has_perm('person_panel.change_studentinfomodel') and StudentInfoModel.objects.get(pk=student_id).company_id.company_id == company_id:
        if request.method=='POST':
            formstudent=StudentInfoForm(request.POST,instance=StudentInfoModel.objects.get(pk=student_id))
            if formstudent.is_valid():
                formstudent.save()
                return redirect('http://127.0.0.1:8000/person_panel/student_table/')
        formstudent=StudentInfoForm(instance=StudentInfoModel.objects.get(pk=student_id))
        tcn_list=PersonIDInfoModel.objects.filter(company_id=company_id)
        city_list=StudentInfoModel().city_list()
        room_list=RoomInfoModel.objects.filter(company_id=company_id)
        student_type_list=StudentInfoModel.student_type_list
        year_list=StudentInfoModel.year_list
        blood_type_list=StudentInfoModel.blood_type_list
        return render(request, 'person_panel/add_student.html', {'form': formstudent,'tcn_list':tcn_list,'city_list':city_list,'room_list':room_list,'student_type_list':student_type_list,'year_list':year_list,'blood_type_list':blood_type_list,'title':'Öğrenci Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_student(request,student_id):
    if request.user.has_perm('person_panel.delete_studentinfomodel') and StudentInfoModel.objects.get(pk=student_id).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        student=StudentInfoModel.objects.get(pk=student_id)
        student.delete()
        return redirect('http://127.0.0.1:8000/person_panel/student_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

# user add and sending mail
def new_user_add(first_name,last_name,email,id,group_id,company_id):
    new_pass = User.objects.make_random_password(10)
    new_user=User(id=id,username=email,first_name=first_name,last_name=last_name,email=email)
    new_user.set_password(new_pass)
    new_user.save()
    new_user.groups.add(group_id)
    subj = 'New Password'
    mesg = 'Thanks for joining our system. \nUsername/E-mail = %s \nYour first password is: %s' % (email, new_pass)
    send_a_email([email],subj,mesg)
    new_record=UserCompanyModel(company_id=company_id,user_id=id)
    new_record.save()

def send_a_email(email_list,subject,message,from_ma='tlhclk1312@gmail.com'):
    to_ma = ['tlhclk1312@windowslive.com']
    for email in email_list:
        if'std.sehir.edu.tr' in email or 'windowslive' in email or 'mail' in email:
            to_ma.append(email)
    mail.send_mail(subject, message, from_ma, to_ma)

def add_parent(request):
    if request.user.has_perm('person_panel.add_parentinfomodel'):
        company_id=UserCompanyModel.objects.filter(user_id=request.user.id)[0].company_id
        new_id=str(int(ParentInfoModel.objects.all().order_by('-id')[0].id)+1)
        formparent= ParentInfoForm(initial={'id':new_id})
        if request.method == "POST":
            formparent = ParentInfoForm(request.POST)
            if formparent.is_valid():
                formparent.save()
                parent=ParentInfoModel.objects.last()
                parent.company_id=CompanyInfoModel.objects.get(pk=company_id)
                parent.save()
            return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
        person_list=StudentInfoModel.objects.filter(company_id=company_id)
        return render(request, 'person_panel/add_parent.html', {'form':formparent,'person_list':person_list, 'title':'Yeni Veli Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_parent(request,parent_id):
    if request.user.has_perm('person_panel.view_parentinfomodel'):
        parent = ParentInfoModel.objects.get(pk=parent_id)
        if parent.company_id_id==UserCompanyModel.objects.get(pk=request.user.id).company_id:
            return render(request, 'person_panel/detail_parent.html', {'parent': parent,'title':'Veli Detayı'})
        else: return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_parent(request):
    if request.user.has_perm('person_panel.view_parentinfomodel'):
        parent_list=ParentInfoModel.objects.filter(company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id)
        return render(request, 'person_panel/table_parent.html', {'parent_list':parent_list, 'title':'Veli Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_parent(request,parent_id):
    company_id=UserCompanyModel.objects.filter(user_id=request.user.id)[0].company_id
    if request.user.has_perm('person_panel.change_parentinfomodel') and ParentInfoModel.objects.get(pk=parent_id).company_id.company_id == company_id:
        formparent=ParentInfoForm(instance=ParentInfoModel.objects.get(pk=parent_id))
        if request.method=='POST':
            formparent=ParentInfoForm(request.POST,instance=ParentInfoModel.objects.get(pk=parent_id))
            if formparent.is_valid():
                formparent.save()
                return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
        person_list=StudentInfoModel.objects.filter(company_id=company_id)
        return render(request, 'person_panel/add_parent.html', {'form':formparent,'person_list':person_list, 'title':'Yeni Veli Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_parent(request,parent_id):
    if request.user.has_perm('person_panel.delete_parentinfomodel') and ParentInfoModel.objects.get(pk=parent_id).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        ParentInfoModel.objects.get(pk=parent_id).delete()
        return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def add_personal(request):
    company_id=UserCompanyModel.objects.filter(user_id=request.user.id)[0].company_id
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        new_id=str(int(PersonalInfoModel.objects.all().order_by('-id')[0].id)+1)
        formpersonal = PersonalInfoForm(initial={'id':new_id})
        if request.method == "POST":
            formpersonal = PersonalInfoForm(request.POST, request.FILES)
            print (formpersonal)
            if formpersonal.is_valid():
                id=formpersonal.cleaned_data.get('id')
                personal_tcn= formpersonal.cleaned_data.get('personal_tcn')
                first_name = personal_tcn.s_name
                last_name = personal_tcn.s_lastname
                email = formpersonal.cleaned_data.get('e_mail')
                new_user_add(first_name, last_name, email,id,'3',company_id)
                formpersonal.save()
                profile_pic_config(PersonalInfoModel.objects.get(pk=id))
                personal=PersonalInfoModel.objects.last()
                personal.company_id=CompanyInfoModel.objects.get(pk=company_id)
                personal.save()
                return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
        blood_type_list=StudentInfoModel.blood_type_list
        city_list=StudentInfoModel().city_list()
        tcn_list=PersonIDInfoModel.objects.filter(company_id=company_id)
        return render(request, 'person_panel/add_personal.html', {'form': formpersonal,'tcn_list':tcn_list,'city_list':city_list,'blood_type_list':blood_type_list,'title':'Yeni Personel Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_personal(request,personal_id):
    if request.user.has_perm('person_panel.view_personalinfomodel'):
        personal = PersonalInfoModel.objects.get(pk=personal_id)
        if personal.company_id_id==UserCompanyModel.objects.get(pk=request.user.id).company_id:
            return render(request,'person_panel/detail_personal.html', {'personal': personal, 'title':'Personel Detayı'})
        else: return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_personal(request):
    if request.user.has_perm('person_panel.view_personalinfomodel'):
        personal_list=PersonalInfoModel.objects.filter(company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id)
        return render(request, 'person_panel/table_personal.html', {'personal_list':personal_list, 'title':'Personel Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_personal(request,personal_id):
    company_id = UserCompanyModel.objects.get(pk=request.user.id).company_id
    if request.user.has_perm('person_panel.change_personalinfomodel') and PersonalInfoModel.objects.get(pk=personal_id).company_id.company_id == company_id:
        if request.method == "POST":
            formpersonal =PersonalInfoForm(request.POST,instance=PersonalInfoModel.objects.get(pk=personal_id))
            if formpersonal.is_valid():
                formpersonal.save()
                return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
        formpersonal = PersonalInfoForm(instance=PersonalInfoModel.objects.get(pk=personal_id))
        blood_type_list=StudentInfoModel.blood_type_list
        city_list=StudentInfoModel.city_list
        tcn_list=PersonIDInfoModel.objects.filter(company_id)
        return render(request, 'person_panel/add_personal.html', {'form': formpersonal,'tcn_list':tcn_list,'city_list':city_list,'blood_type_list':blood_type_list,'title':'Yeni Personel Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_personal(request,personal_id):
    if request.user.has_perm('person_panel.delete_personalinfomodel') and PersonalInfoModel.objects.get(pk=personal_id).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        PersonalInfoModel.objects.get(pk=personal_id).delete()
        return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def add_person_id(request):
    if request.user.has_perm('person_panel.add_personidinfomodel'):
        formperson_id = PersonIDInfoForm()
        if request.method == "POST":
            formperson_id = PersonIDInfoForm(request.POST, request.FILES)
            if formperson_id.is_valid():
                formperson_id.save()
                person_id=PersonIDInfoModel.objects.last()
                company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id
                person_id.company_id=CompanyInfoModel.objects.get(pk=company_id)
                person_id.save()
            return redirect('http://127.0.0.1:8000/person_panel/student_add/')
        nation_list=PersonIDInfoModel.nation_list
        id_card_list=PersonIDInfoModel.idcard_type_list
        gender_list=PersonIDInfoModel.gender_list
        city_list=PersonIDInfoModel.city_list
        medeni_hal_list=PersonIDInfoModel.medeni_hal_list
        return render(request, 'person_panel/add_person_id.html', {'form': formperson_id,'nation_list':nation_list,'id_card_list':id_card_list,'gender_list':gender_list,'city_list':city_list,'medeni_hal_list':medeni_hal_list,'title':'Yeni Kimlik Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_person_id(request,person_id):
    if request.user.has_perm('person_panel.view_personidinfomodel'):
        person=PersonIDInfoModel.objects.get(pk=person_id)
        person_info=(StudentInfoModel.objects.filter(student_tcn=person_id) or PersonalInfoModel.objects.filter(personal_tcn=person_id))
        company_id = UserCompanyModel.objects.get(pk=request.user.id).company_id
        if person.company_id_id==company_id and person_info.company_id_id==company_id:
            return render(request,'person_panel/detail_person_id.html',{'person':person,'person_info':person_info[0],'title':'Kimlik Detayı'})
        else: return redirect('http://127.0.0.1:8000/person_panel/person_id_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_person_id(request):
    if request.user.has_perm('person_panel.view_personidinfomodel'):
        person_id_list=PersonIDInfoModel.objects.filter(company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id)
        return render(request, 'person_panel/table_person_id.html', {'person_id_list':person_id_list,'title':'Kimlik Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_person_id(request,person_id):
    if request.user.has_perm('person_panel.change_personidinfomodel') and PersonIDInfoModel.objects.get(pk=person_id).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        if request.method == "POST":
            formperson_id =PersonIDInfoForm(request.POST,instance=PersonIDInfoModel.objects.get(pk=person_id))
            print (formperson_id)
            if formperson_id.is_valid():
                formperson_id.save()
                return redirect('http://127.0.0.1:8000/person_panel/person_id_table/')
        formperson_id = PersonIDInfoForm(instance=PersonIDInfoModel.objects.get(pk=person_id))
        nation_list = PersonIDInfoModel.nation_list
        id_card_list = PersonIDInfoModel.idcard_type_list
        gender_list = PersonIDInfoModel.gender_list
        city_list = PersonIDInfoModel.city_list
        medeni_hal_list = PersonIDInfoModel.medeni_hal_list
        return render(request, 'person_panel/add_person_id.html',{'form': formperson_id, 'nation_list': nation_list, 'id_card_list': id_card_list,'gender_list': gender_list, 'city_list': city_list, 'medeni_hal_list': medeni_hal_list,'title': 'Yeni Kimlik Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_person_id(request,person_id):
    if request.user.has_perm('person_panel.delete_personidinfomodel') and PersonIDInfoModel.objects.get(pk=person_id).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        PersonIDInfoModel.objects.get(pk=person_id).delete()
        return redirect('http://127.0.0.1:8000/person_panel/person_id_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def show_profile(request,person_id):
    if person_id[:4]=='1701':
        return redirect('http://127.0.0.1:8000/person_panel/student/'+person_id)
    elif person_id[:4]=='1703':
        return redirect('http://127.0.0.1:8000/person_panel/personal/' + person_id)
    elif person_id[:4]=='1704':
        return redirect('http://127.0.0.1:8000/person_panel/parent/' + person_id)
    else:
        if len(StudentInfoModel.objects.filter(student_tcn=person_id))!=0:
            student = StudentInfoModel.objects.filter(student_tcn=person_id)[0]
            return redirect('http://127.0.0.1:8000/person_panel/student/' + student.id)
        elif len(PersonalInfoModel.objects.filter(personal_tcn=person_id))!=0:
            personal = PersonalInfoModel.objects.filter(personal_tcn=person_id)[0]
            return redirect('http://127.0.0.1:8000/person_panel/personal/' + personal.id)
        else:
            return ('Aranan Kayıt Bulunamadı')

def profile_pic_config(user):
    try:
        id=user.id
        import os
        os.rename(user.image_field.path,os.path.join(os.path.split(user.image_field.path)[0],str(id)+'.jpg'))
        user.image_field.name='profile_pic/'+str(id)+'.jpg'
        user.save()
    except FileNotFoundError:
        pass

