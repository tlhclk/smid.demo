from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import mail
from .forms import StudentInfoForm,ParentInfoForm
from .models import StudentInfoModel,ParentInfoModel


def options_menu(request):
    return render(request,'student_panel/options_menu.html')

def add_stundent(request):
    formstudent = StudentInfoForm()
    if 1==1:#request.user.has_perm('studentpanel.add_studentinfomodel'):
        if request.method == "POST":
            formstudent = StudentInfoForm(request.POST, request.FILES)
            if formstudent.is_valid():
                first_name = formstudent.cleaned_data.get('student_name')
                last_name = formstudent.cleaned_data.get('student_lastname')
                email = formstudent.cleaned_data.get('student_email')
                new_user_add(first_name, last_name, email)
                formstudent.save()
            return redirect('/student_panel/')
        return render(request, 'student_panel/add_student.html', {'formstudent': formstudent})
    else:
        return HttpResponse('You has no authorization')

def detail_student(request,student_id):
    student = StudentInfoModel.objects.get( pk=student_id)
    user = User.objects.get(username=student.student_email)
    user_perms = request.user.has_perm('student_panel.list_stucentinfomodel')
    #return render(request, 'student_panel/detail_student.html', {'student': student, 'user':user, 'user_perms':user_perms})
    return render(request, 'SmartDorms/pages/examples/profil.html',{'student': student, 'user': user, 'user_perms': user_perms})

def table_student(request):
    database_info=StudentInfoModel.objects.all()
    user_perms = request.user.has_perm('yps.view_student')
    return render(request, 'student_panel/table_student.html', {'databaseinfo':database_info, 'user_perms':user_perms})

def edit_student(request,student_id):
    student = StudentInfoModel.objects.get( pk=student_id)
    return render(request,'student_panel/edit_student.html',{'student':student})

def delete_student(request,student_id):
    student=StudentInfoModel.objects.get(pk=student_id)

    student.delete()
    if User.objects.get(username=student.student_email):
        user = User.objects.get(username=student.student_email)
        user.delete()
    return redirect('../student_table/')

# user add and sending mail
def new_user_add(first_name,last_name,email):
    student_user_list=User.objects.filter(groups__name='Student').order_by('-id')
    new_pass=User.objects.make_random_password()
    new_user=User(username=email,first_name=first_name,last_name=last_name,email=email)
    new_user.id = student_user_list[0].id+1
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
    formparent= ParentInfoForm()
    if request.method == "POST":
        formparent = ParentInfoForm(request.POST)
        if formparent.is_valid():
            formparent.save()
        return redirect('/student_panel/parent_table/')
    return render(request, 'student_panel/add_parent.html', {'formparent':formparent})

def detail_parent(request,parent_id):
    parent = ParentInfoModel.objects.get( pk=parent_id)
    return render(request, 'student_panel/detail_parent.html', {'parent': parent})

def table_parent(request):
    parent_list=ParentInfoModel.objects.all()
    return render(request, 'student_panel/table_parent.html', {'parent_list':parent_list})

def edit_parent(request,parent_id):
    formparent= ParentInfoForm()
    print (request)
    print (request.POST)
    print (request.method)
    if request.method == "POST":
        formparent = ParentInfoForm(request.POST or None)
        if formparent.is_valid():
            print (formparent.clean())
            pass
            #formparent.save()
        return redirect('../parent_table/')
    parent = ParentInfoModel.objects.get( pk=parent_id)
    return render(request,'student_panel/edit_parent.html',{'formparent':formparent,'parent':parent,'student':parent})

def delete_parent(request,parent_id):
    parent=ParentInfoModel.objects.get(pk=parent_id)
    parent.delete()
    return redirect('../parent_table/')