# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='operation_panel'
urlpatterns = [
    url(r'^$',views.option_menu,name='Operation Option Menu'),
    url(r'^attendance_add/', views.add_attendance, name='Entrance'),
    url(r'^attendance_table/', views.table_attendance, name='Entrance Leave Table'),
    url(r'^student_leave_add/',views.add_student_leave,name='Permission Assign'),
    url(r'^mail_send/(?P<person_mail>\w+@\w+\.com)*',views.send_a_mail,name='Send Collective Mesaj'),
    url(r'^change_position/(?P<student_id>[0-9]+)',views.change_student_position,name='change student position'),
    url(r'^create_egm_xml/',views.create_egm_xml,name='Create EGM Xml'),
    url(r'^asd/',views.show_form,name='asd')

]