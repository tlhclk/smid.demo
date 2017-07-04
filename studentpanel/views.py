from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import mail
from .forms import StudentInfoForm,ParentInfoForm,PersonalInfoForm,PersonLeaveForm
from .models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonLeaveModel
from fixturepanel.models import RoomInfoModel
import datetime


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
                    id=formstudent.cleaned_data.get('id')
                    first_name = formstudent.cleaned_data.get('student_name')
                    last_name = formstudent.cleaned_data.get('student_lastname')
                    email = formstudent.cleaned_data.get('student_email')
                    new_user_add(first_name, last_name, email,id,group_id='1')
            return redirect('/student_panel/')
        student_new_id = int(StudentInfoModel.objects.all().order_by('-id')[0].id)+1
        return render(request, 'student_panel/add_student.html', {'formstudent': formstudent,'new_id':student_new_id,'today':str(datetime.date.today())})
    else:
        return HttpResponse('You has no authorization to add a student')

def detail_student(request,student_id):
    if request.user.has_perm('studentpanel.view_profile'):
        student = StudentInfoModel.objects.get( pk=student_id)
        user = User.objects.get(username=student.student_email)
        show=True
        leave_boolean=None
        if len(PersonLeaveModel.objects.filter(leave_person_id=student_id))!=0:
            for permi in PersonLeaveModel.objects.filter(leave_person_id=student_id):
                if datetime.datetime.strptime(str(permi.leave_start),"%Y-%m-%d")<=datetime.datetime.strptime(str(datetime.date.today()),'%Y-%m-%d')<=datetime.datetime.strptime(str(permi.leave_end),"%Y-%m-%d"):
                    leave_boolean=permi.leave_start,permi.leave_end
        return render(request, 'student_panel/detail_student.html', {'student': student, 'user': user,'show':show,'leave_boolean':leave_boolean})

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
        all_in,all_all=(len(StudentInfoModel.objects.filter(student_position=True)),len(StudentInfoModel.objects.all()))
        return render(request, 'student_panel/table_student.html', {'student_list':student_list,'view_pro_per':view_pro_per,'all_in':all_in,'all_all':all_all})
    else: return HttpResponse('You has no authorization to view student info list')

def edit_student(request,student_id):
    if request.user.has_perm('studentpanel.change_studentinfomodel'):
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
            student.room_number=RoomInfoModel.objects.get(pk=request.POST['room_number'])
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
    elif request.user.has_perm('studentpanel.change_profile'):
        student = StudentInfoModel.objects.get( pk=student_id)
        if request.method=='POST':
            student.student_phone=request.POST['student_phone']
            student.student_email=request.POST['student_email']
            student.student_city=request.POST['student_city']
            student.student_town=request.POST['student_town']
            student.school_name=request.POST['school_name']
            student.education_year=request.POST['education_year']
            student.health_notes=request.POST['health_notes']
            if len(request.FILES) is not 0:student.file_field=request.FILES['file_field']
            student.save()
            return redirect('../../student_panel/student/%s'%student_id)
        return render(request,'student_panel/edit_student.html',{'student':student})

    else: return HttpResponse('You has no authorization to change student info')

def delete_student(request,student_id):
    if request.user.has_perm('studentpanel.delete_studentinfomodel'):
        student=StudentInfoModel.objects.get(pk=student_id)
        parent=ParentInfoModel.objects.filter(student_id=student_id)
        student.delete()
        if request.user.has_perm('auth.delete_user'):
            if len(User.objects.filter(username=student.student_email))!=0:
                user = User.objects.get(username=student.student_email)
                user.delete()
        return redirect('../student_table/')
    else: return HttpResponse('You has no authorization to delete a student')

# user add and sending mail
def new_user_add(first_name,last_name,email,id,group_id):
    new_pass = User.objects.make_random_password(10)
    new_user=User(id=id,username=email,first_name=first_name,last_name=last_name,email=email)
    new_user.set_password(new_pass)
    new_user.save()
    new_user.groups.add(group_id)
    send_a_email(email,new_pass)

def send_a_email(email,new_pass):
    subj = 'New Password'
    mesg = 'Thanks for joining our system. \nUsername/E-mail = %s \nYour first password is: %s' % (email, new_pass)
    from_ma = 'tlhclk1312@gmail.com'
    to_ma = ['tlhclk1312@windowslive.com']
    if 'gmail' in email:
        to_ma.append(email)
    mail.send_mail(subj, mesg, from_ma, to_ma)

def change_student_position(request,student_id):
    student=StudentInfoModel.objects.get(pk=student_id)
    if student.student_position==True:
        student.student_position=False
    else:
        student.student_position=True
    student.save()
    return redirect('../../student/%s'%student_id)

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
    if request.user.has_perm('studentpanel.change_parentinfomodel'):
        if request.method == "POST":
            parent = ParentInfoModel.objects.get(pk=parent_id)
            parent.parent_name=request.POST['parent_name']
            parent.parent_lastname=request.POST['parent_lastname']
            parent.parent_job=request.POST['parent_job']
            parent.parent_email=request.POST['parent_email']
            parent.parent_phone=request.POST['parent_phone']
            parent.save()
            return redirect('../../')
        parent = ParentInfoModel.objects.get(pk=parent_id)
        return render(request,'student_panel/edit_parent.html',{'parent':parent})
    else: return HttpResponse('You has no authorization to change parent info')

def delete_parent(request,parent_id):
    if request.user.has_perm('studentpanel.delete_parentinfomodel'):
        parent=ParentInfoModel.objects.get(pk=parent_id)
        parent.delete()
        return redirect('../parent_table/')
    else: return HttpResponse('You has no authorization to delete a parent')

def add_personal(request):
    if request.user.has_perm('studentpanel.add_personalinfomodel'):
        formpersonal = PersonalInfoForm()
        if request.method == "POST":
            formpersonal = PersonalInfoForm(request.POST, request.FILES)
            if formpersonal.is_valid():
                formpersonal.save()
                if request.user.has_perm('auth.add_user'):
                    id=formpersonal.cleaned_data.get('id')
                    first_name = formpersonal.cleaned_data.get('personal_name')
                    last_name = formpersonal.cleaned_data.get('personal_lastname')
                    email = formpersonal.cleaned_data.get('personal_email')
                    new_user_add(first_name, last_name, email,id,group_id=3)
            return redirect('/student_panel/')
        personal_new_id = int(PersonalInfoModel.objects.all().order_by('-id')[0].id)+1
        return render(request, 'student_panel/add_personal.html', {'formpersonal': formpersonal,'new_id':personal_new_id})
    else:
        return HttpResponse('You has no authorization to add a personal')

def detail_personal(request,personal_id):
    if request.user.has_perm('studentpanel.view_profile'):
        personal = PersonalInfoModel.objects.get( pk=personal_id)
        try:
            user = User.objects.get(pk=personal_id)
            show=True
            return render(request, 'student_panel/detail_personal.html', {'personal': personal, 'user': user,'show':show})
        except:
            return HttpResponse('There is no user as: %s <a href="../"> Go back</a>' % personal.personal_email)

    elif request.user.has_perm('studentpanel.view_personalinfomodel'):
        personal = PersonalInfoModel.objects.get( pk=personal_id)
        user = User.objects.get(username=personal.personal_email)
        parent = ParentInfoModel.objects.filter(personal_id=personal_id)
        return render(request, 'student_panel/detail_personal.html', {'personal': personal, 'user':user,'parent':parent})
    else: return HttpResponse('You has no authorization to view personal profile <a href="../"> Go back</a>')

def table_personal(request):
    if request.user.has_perm('studentpanel.view_personalinfomodel'):
        view_pro_per=request.user.has_perm('personalpanel.view_profile')
        personal_list=PersonalInfoModel.objects.all()
        return render(request, 'student_panel/table_personal.html', {'personal_list':personal_list,'view_pro_per':view_pro_per})
    else: return HttpResponse('You has no authorization to view personal info list')

def edit_personal(request,personal_id):
    if request.user.has_perm('studentpanel.change_personalinfomodel'):
        if request.method == "POST":
            personal = PersonalInfoModel.objects.get(pk=personal_id)
            personal.personal_name=request.POST['personal_name']
            personal.personal_lastname=request.POST['personal_lastname']
            personal.personal_phone=request.POST['personal_phone']
            personal.personal_email=request.POST['personal_email']
            personal.personal_startday=request.POST['personal_startday']
            personal.personal_endday=request.POST['personal_endday']
            personal.personal_city=request.POST['personal_city']
            personal.personal_town=request.POST['personal_town']
            personal.personal_adress=request.POST['personal_adress']
            personal.health_notes=request.POST['health_notes']
            personal.special_notes=request.POST['special_notes']
            personal.image_field=request.POST['image_field']
            personal.save()
            return redirect('../personal_table/')
        personal = PersonalInfoModel.objects.get(pk=personal_id)
        return render(request,'student_panel/edit_personal.html',{'personal':personal})
    else: return HttpResponse('You has no authorization to change personal info')

def delete_personal(request,personal_id):
    if request.user.has_perm('studentpanel.delete_personalinfomodel'):
        personal=PersonalInfoModel.objects.get(pk=personal_id)
        personal.delete()
        return redirect('../personal_table/')
    else: return HttpResponse('You has no authorization to delete a personal')

def leave_assign(request):
    leave_form=PersonLeaveForm
    if request.method=='POST':
        leave_form = PersonLeaveForm(request.POST)
        #print leave_form
        if leave_form.is_valid():
            leave_form.save()
    next_id='1710001'#int(PersonleaveModel.objects.all().order_by('-leave_id')[0].id)+1
    person_list=PersonLeaveModel.person_list
    #return render(request,'user_panel/default_form.html',{'form':leave_form})
    return render(request,'student_panel/leave_assign.html',{'formleave':leave_form,'next_id':next_id,'person_list':person_list})