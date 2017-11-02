# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views,apps

app_name='operation_panel'
urlpatterns = [
    url(r'^attendance_add/', views.add_attendance, name='Entrance'),
    url(r'^attendance_table/', views.table_attendance, name='Entrance Leave Table'),
    url(r'^leave_add/',views.add_student_leave,name='Permission Assign'),
    url(r'^leave_table/',views.table_student_leave,name='Permission Assign Table'),
    url(r'^mail_send/(?P<person_mail>\w+@\w+\.com)*',views.send_a_mail,name='Send Collective Mesaj'),
    url(r'^change_position/(?P<student_id>[0-9]+)',views.change_student_position,name='change student position'),
    url(r'^create_egm_xml/',apps.create_adress_info,name='Create EGM Xml'),
    url(r'^vacation_add/',views.add_vacation,name='Vacation Add'),
    url(r'^vacation_table/',views.table_vacation,name='Vacation Table'),
    url(r'^vacation_delete/',views.delete_vacation,name='Vacation Delete'),
    url(r'^vacation_edit/',views.edit_vacation,name='Vacation Edit'),

]