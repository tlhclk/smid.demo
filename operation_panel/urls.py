# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='operation_panel'
urlpatterns = [
    url(r'^option_menu/',views.option_menu,name='Operation Option Menu'),
    url(r'^attendance_add/', views.add_attendance, name='Entrance'),
    url(r'^attendance_table/', views.table_attendance, name='Entrance Leave Table'),
    url(r'^student_leave/',views.add_student_leave,name='Permission Assign'),
    url(r'^send_collective_message',views.send_collective_message,name='Send Collective Mesaj'),
    url(r'^change_position/(?P<student_id>[0-9]+)/',views.change_student_position,name='change student position'),
]