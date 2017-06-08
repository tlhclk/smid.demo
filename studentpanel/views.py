from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import mail
from django.contrib.auth import hashers
from .forms import StudentInfoForm,ParentInfoForm
from .models import StudentInfoModel,ParentInfoModel
import random


def options_menu(request):
    return render(request,'student_panel/options_menu.html')

def add_stundent(request):
    if request.user.has_perm('studentpanel.add_studentinfomodel'):
        formstudent = StudentInfoForm()
        if request.method == "POST":
            formstudent = StudentInfoForm(request.POST, request.FILES)
            if formstudent.is_valid():
                formstudent.save()
                if request.user.has_perm('auth.add_user'):
                    first_name = formstudent.cleaned_data.get('student_name')
                    last_name = formstudent.cleaned_data.get('student_lastname')
                    email = formstudent.cleaned_data.get('student_email')
                    new_user_add(first_name, last_name, email)
            return redirect('/student_panel/')
        return render(request, 'student_panel/add_student.html', {'formstudent': formstudent})
    else:
        return HttpResponse('You has no authorization to add a student')

def detail_student(request,student_id):
    if request.user.has_perm('studentpanel.view_profile'):
        student = StudentInfoModel.objects.get( pk=student_id)
        try:
            user = User.objects.get(username=student.student_email)
            show=True
            return render(request, 'student_panel/detail_student.html', {'student': student, 'user': user,'show':show})
        except:
            user=None
            show=True
            return render(request, 'student_panel/detail_student.html', {'student': student, 'user': user,'show':show})

        #return render(request, 'static/pages/examples/profil.html',{'student': student, 'user': user, 'user_perms': user_perms})
    elif request.user.has_perm('studentpanel.view_studentinfomodel'):
        student = StudentInfoModel.objects.get( pk=student_id)
        user = User.objects.get(username=student.student_email)
        parent = ParentInfoModel.objects.filter(student_id=student_id)
        return render(request, 'student_panel/detail_student.html', {'student': student, 'user':user,'parent':parent})
    else: return HttpResponse('You has no authorization to view student profile <a href="../"> Go back</a>')

def table_student(request):
    if request.user.has_perm('studentpanel.view_studentinfomodel'):
        view_pro_per=request.user.has_perm('studentpanel.view_profile')
        student_list=StudentInfoModel.objects.all()
        return render(request, 'student_panel/table_student.html', {'student_list':student_list,'view_pro_per':view_pro_per})
    else: return HttpResponse('You has no authorization to view student info list')

def edit_student(request,student_id):
    if request.user.has_perm('studentpanel.change_profile'):
        student = StudentInfoModel.objects.get( pk=student_id)
        if request.method=='POST':
            student.student_phone=request.POST['student_phone']
            student.student_email=request.POST['student_email']
            student.student_city=request.POST['student_city']
            student.student_town=request.POST['student_town']
            student.school_name=request.POST['school_name']
            student.education_year=request.POST['education_year']
            student.health_notes=request.POST['health_notes']
            student.file_field=request.FILES['file_field']
            student.save()
            return redirect('../../student_panel/student/%s'%student_id)
        return render(request,'student_panel/edit_student.html',{'student':student})

    elif request.user.has_perm('studentpanel.change_studentinfomodel'):
        student = StudentInfoModel.objects.get( pk=student_id)
        if request.method=='POST':
            student.student_tcn=request.POST['student_tcn']
            student.student_name=request.POST['student_name']
            student.student_lastname=request.POST['student_lastname']
            student.student_phone=request.POST['student_phone']
            student.student_email=request.POST['student_email']
            student.student_birthday=request.POST['student_birthday']
            student.student_regday=request.POST['student_regday']
            student.student_city=request.POST['student_city']
            student.student_town=request.POST['student_town']
            student.room_number=request.POST['room_number']
            student.student_type=request.POST['student_type']
            student.birth_place=request.POST['birth_place']
            student.school_name=request.POST['school_name']
            student.education_year=request.POST['education_year']
            student.blood_type=request.POST['blood_type']
            student.health_notes=request.POST['health_notes']
            student.special_notes=request.POST['special_notes']
            student.file_field=request.FILES['file_field']
            student.save()
            return redirect('../../student_panel/student/%s'%student_id)
        return render(request,'student_panel/edit_student.html',{'student':student})
    else: return HttpResponse('You has no authorization to change student info')

def delete_student(request,student_id):
    if request.user.has_perm('studentpanel.delete_studentinfomodel'):
        student=StudentInfoModel.objects.get(pk=student_id)
        student.delete()
        if request.user.has_perm('auth.delete_user'):
            if User.objects.get(username=student.student_email):
                user = User.objects.get(username=student.student_email)
                user.delete()
        return redirect('../student_table/')
    else: return HttpResponse('You has no authorization to delete a student')

# user add and sending mail
def new_user_add(first_name,last_name,email):
    new_id = User.objects.filter(groups__name='Student').order_by('-id')[0].id+1
    new_pass = User.objects.make_random_password(10)
    new_user=User(id=new_id,username=email,first_name=first_name,last_name=last_name,email=email)
    new_user.groups.add(1)
    new_user.set_password(new_pass)
    new_user.save()
    send_a_email(email,new_pass)

def send_a_email(email,new_pass):
    subj = 'New Password'
    mesg = 'Thanks for joining our system. \nUsername/E-mail = %s \nYour first password is: %s' % (email, new_pass)
    from_ma = 'tlhclk1312@gmail.com'
    to_ma = ['tlhclk1312@windowslive.com']
    if 'gmail' in email:
        to_ma.append(email)
    mail.send_mail(subj, mesg, from_ma, to_ma)

def add_parent(request):
    if request.user.has_perm('studentpanel.add_studentinfomodel'):
        formparent= ParentInfoForm()
        if request.method == "POST":
            formparent = ParentInfoForm(request.POST)
            if formparent.is_valid():
                formparent.save()
            return redirect('/student_panel/parent_table/')
        return render(request, 'student_panel/add_parent.html', {'formparent':formparent})
    else: return HttpResponse('You has no authorization to add a parent')

def detail_parent(request,parent_id):
    if request.user.has_perm('studentpanel.view_profile'):
        parent = ParentInfoModel.objects.get( pk=parent_id)
        return render(request, 'student_panel/detail_parent.html', {'parent': parent})
    else: return HttpResponse('You has no authorization to view parent profile <a href="../"> Go back</a>')

def table_parent(request):
    if request.user.has_perm('studentpanel.view_parentinfomodel'):
        parent_list=ParentInfoModel.objects.all()
        return render(request, 'student_panel/table_parent.html', {'parent_list':parent_list})
    else: return HttpResponse('You has no authorization to view parent info list')

def edit_parent(request,parent_id):
    if request.user.has_perm('studentpanel.change_profile'):
        pass
    elif request.user.has_perm('studentpanel.change_parentinfomodel'):
        if request.method == "POST":
            return redirect('../parent_table/')
        parent = ParentInfoModel.objects.get( pk=parent_id)
        return render(request,'student_panel/edit_parent.html',{'parent':parent,'student':parent})
    else: return HttpResponse('You has no authorization to change parent info')

def delete_parent(request,parent_id):
    if request.user.has_perm('studentpanel.delete_parentinfomodel'):
        parent=ParentInfoModel.objects.get(pk=parent_id)
        parent.delete()
        return redirect('../parent_table/')
    else: return HttpResponse('You has no authorization to delete a parent')