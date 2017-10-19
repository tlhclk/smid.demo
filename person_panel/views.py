# -*- coding: utf-8 -*-
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.core import mail
from .forms import StudentInfoForm,ParentInfoForm,PersonalInfoForm,PersonIDInfoForm
from .models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonIDInfoModel
from user_panel.models import CompanyInfoModel
import datetime
from stock_panel.models import RoomInfoModel


def add_student(request):
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        formstudent = StudentInfoForm(user=request.user)
        if request.method == "POST":
            formstudent = StudentInfoForm(user=request.user,POST=request.POST, FILES=request.FILES)
            if formstudent.is_valid():
                #new_user_add(formstudent) TODO: ilerleyen süreçte tekrar düzenlenecek
                formstudent.save()
            return redirect('http://127.0.0.1:8000/account_panel/asset_add/')
        return render(request, 'person_panel/add_student.html', {'form': formstudent,'title':'Yeni Öğrenci Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_student(request,student_id):
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        student = StudentInfoModel.objects.get(pk=student_id)
        parent = ParentInfoModel.objects.filter(student_id=student_id)[0]
        if student.company_id_id==request.user.company_id_id:
            return render(request, 'person_panel/detail_student.html', {'student': student,'parent':parent,'title':'Öğrenci Detayı'})
        else: return redirect('http://127.0.0.1:8000/person_panel/student_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_student(request):
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        student_list=StudentInfoModel.objects.filter(company_id=request.user.company_id_id)
        return  render(request, 'person_panel/table_student.html',{'student_list':student_list, 'title': 'Öğrenci Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_student(request,student_id):
    if request.user.has_perm('person_panel.change_studentinfomodel') and StudentInfoModel.objects.get(pk=student_id).company_id.company_id == request.user.company_id_id:
        if request.method=='POST':
            formstudent=StudentInfoForm(user=request.user,POST=request.POST, FILES=request.FILES,instance=StudentInfoModel.objects.get(pk=student_id))
            if formstudent.is_valid():
                formstudent.save()
                return redirect('http://127.0.0.1:8000/person_panel/student_table/')
        formstudent=StudentInfoForm(user=request.user,instance=StudentInfoModel.objects.get(pk=student_id))
        return render(request, 'person_panel/add_student.html', {'form': formstudent,'title':'Öğrenci Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_student(request,student_id):
    if request.user.has_perm('person_panel.delete_studentinfomodel') and StudentInfoModel.objects.get(pk=student_id).company_id_id==request.user.company_id_id:
        student=StudentInfoModel.objects.get(pk=student_id)
        student.delete()
        return redirect('http://127.0.0.1:8000/person_panel/student_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

# user add and sending mail
def new_user_add(form):
    id=form.cleaned_data.get('id')
    email = form.cleaned_data.get('email')
    student_tcn = form.cleaned_data.get('tcn')
    first_name= student_tcn.s_name
    last_name = student_tcn.s_lastname
    phone=form.cleaned_data.get('phone')
    date_joined=datetime.datetime.today()
    profile_image=form.cleaned_data.get('image_field').path
    company_id=form.cleaned_data.get('company_id')
    new_user=User(id=id,email=email,first_name=first_name,last_name=last_name,phone=phone,date_joined=date_joined,profile_image=profile_image,company_id=company_id)
    new_pass = User.objects.make_random_password(10)
    new_user.set_password(new_pass)
    new_user.save()
    new_user.groups.add('1')
    subj = 'New Password'
    mesg = 'Thanks for joining our system. \nUsername/E-mail = %s \nYour first password is: %s' % (email, new_pass)
    send_a_email([email],subj,mesg)

def send_a_email(email_list,subject,message,from_ma='tlhclk1312@gmail.com'):
    to_ma = ['tlhclk1312@windowslive.com']
    for email in email_list:
        if'std.sehir.edu.tr' in email or 'windowslive' in email or 'mail' in email:
            to_ma.append(email)
    mail.send_mail(subject, message, from_ma, to_ma)

def add_parent(request):
    if request.user.has_perm('person_panel.add_parentinfomodel'):
        formparent= ParentInfoForm(user=request.user)
        if request.method == "POST":
            formparent = ParentInfoForm(user=request.user,POST=request.POST)
            if formparent.is_valid():
                formparent.save()
            return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
        return render(request, 'person_panel/add_parent.html', {'form':formparent,'title':'Yeni Veli Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_parent(request,parent_id):
    if request.user.has_perm('person_panel.add_parentinfomodel'):
        parent = ParentInfoModel.objects.get(pk=parent_id)
        if parent.company_id_id==request.user.company_id_id:
            return render(request, 'person_panel/detail_parent.html', {'parent': parent,'title':'Veli Detayı'})
        else: return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_parent(request):
    if request.user.has_perm('person_panel.add_parentinfomodel'):
        parent_list=ParentInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request, 'person_panel/table_parent.html', {'parent_list':parent_list, 'title':'Veli Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_parent(request,parent_id):
    if request.user.has_perm('person_panel.change_parentinfomodel') and ParentInfoModel.objects.get(pk=parent_id).company_id_id==request.user.company_id_id:
        formparent=ParentInfoForm(user=request.user,instance=ParentInfoModel.objects.get(pk=parent_id))
        if request.method=='POST':
            formparent=ParentInfoForm(user=request.user,POST=request.POST,instance=ParentInfoModel.objects.get(pk=parent_id))
            if formparent.is_valid():
                formparent.save()
                return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
        return render(request, 'person_panel/add_parent.html', {'form':formparent, 'title':'Yeni Veli Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_parent(request,parent_id):
    if request.user.has_perm('person_panel.delete_parentinfomodel') and ParentInfoModel.objects.get(pk=parent_id).company_id_id == request.user.company_id_id:
        ParentInfoModel.objects.get(pk=parent_id).delete()
        return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def add_personal(request):
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        formpersonal = PersonalInfoForm(user=request.user)
        if request.method == "POST":
            formpersonal = PersonalInfoForm(user=request.user,POST=request.POST, FILES=request.FILES)
            if formpersonal.is_valid():
                new_user_add(formpersonal)
                formpersonal.save()
                return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
        return render(request, 'person_panel/add_personal.html', {'form': formpersonal,'title':'Yeni Personel Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_personal(request,personal_id):
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        personal = PersonalInfoModel.objects.get(pk=personal_id)
        if personal.company_id_id== request.user.company_id_id:
            return render(request,'person_panel/detail_personal.html', {'personal': personal, 'title':'Personel Detayı'})
        else: return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_personal(request):
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        personal_list=PersonalInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request, 'person_panel/table_personal.html', {'personal_list':personal_list, 'title':'Personel Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_personal(request,personal_id):
    if request.user.has_perm('person_panel.change_personalinfomodel') and PersonalInfoModel.objects.get(pk=personal_id).company_id_id==request.user.company_id_id:
        if request.method == "POST":
            formpersonal =PersonalInfoForm(user=request.user,POST=request.POST,FILES=request.FILES,instance=PersonalInfoModel.objects.get(pk=personal_id))
            if formpersonal.is_valid():
                formpersonal.save()
                return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
        formpersonal = PersonalInfoForm(user=request.user,instance=PersonalInfoModel.objects.get(pk=personal_id))
        return render(request, 'person_panel/add_personal.html', {'form': formpersonal,'title':'Yeni Personel Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_personal(request,personal_id):
    if request.user.has_perm('person_panel.delete_personalinfomodel') and PersonalInfoModel.objects.get(pk=personal_id).company_id_id == request.user.company_id_id:
        PersonalInfoModel.objects.get(pk=personal_id).delete()
        return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def add_person_id(request):
    if request.user.has_perm('person_panel.add_personidinfomodel'):
        formperson_id = PersonIDInfoForm(user=request.user)
        if request.method == "POST":
            formperson_id = PersonIDInfoForm(user=request.user,POST=request.POST)
            if formperson_id.is_valid():
                formperson_id.save()
            return redirect('http://127.0.0.1:8000/person_panel/student_add/')
        return render(request, 'person_panel/add_person_id.html', {'form': formperson_id,'title':'Yeni Kimlik Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_person_id(request,person_id):
    if request.user.has_perm('person_panel.add_personidinfomodel'):
        person=PersonIDInfoModel.objects.get(pk=person_id)
        person_info=(StudentInfoModel.objects.filter(student_tcn=person_id) or PersonalInfoModel.objects.filter(personal_tcn=person_id))
        if person.company_id_id==request.user.company_id_id and person_info.company_id_id==request.user.company_id_id:
            return render(request,'person_panel/detail_person_id.html',{'person':person,'person_info':person_info[0],'title':'Kimlik Detayı'})
        else: return redirect('http://127.0.0.1:8000/person_panel/person_id_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_person_id(request):
    if request.user.has_perm('person_panel.add_personidinfomodel'):
        person_id_list=PersonIDInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request, 'person_panel/table_person_id.html', {'person_id_list':person_id_list,'title':'Kimlik Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_person_id(request,person_id):
    if request.user.has_perm('person_panel.change_personidinfomodel') and PersonIDInfoModel.objects.get(pk=person_id).company_id_id==request.user.company_id_id:
        if request.method == "POST":
            formperson_id =PersonIDInfoForm(user=request.user,POST=request.POST,instance=PersonIDInfoModel.objects.get(pk=person_id))
            if formperson_id.is_valid():
                formperson_id.save()
                return redirect('http://127.0.0.1:8000/person_panel/person_id_table/')
        formperson_id = PersonIDInfoForm(user=request.user,instance=PersonIDInfoModel.objects.get(pk=person_id))
        return render(request, 'person_panel/add_person_id.html',{'form': formperson_id,'title': 'Yeni Kimlik Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_person_id(request,person_id):
    if request.user.has_perm('person_panel.delete_personidinfomodel') and PersonIDInfoModel.objects.get(pk=person_id).company_id_id == request.user.company_id_id:
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
        if PersonIDInfoModel.objects.get(pk=person_id):
            person = PersonIDInfoModel.objects.get(pk=person_id)
            return redirect('http://127.0.0.1:8000/person_panel/perosn_id/' + person.id)
        else:
            return ('Aranan Kayıt Bulunamadı')

