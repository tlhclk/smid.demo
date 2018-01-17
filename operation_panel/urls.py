# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views,apps

app_name='operation_panel'
urlpatterns = [
    url(r'^leave_add/$',views.add_student_leave,name='permission_add'),
    url(r'^leave_table/(?P<student_id>[0-9]*)$',views.table_student_leave,name='permission_table'),
    url(r'^leave_edit/(?P<sleave_id>[0-9]+)$',views.edit_student_leave,name='permission_edit'),
    url(r'^leave_delete/(?P<sleave_id>[0-9]+)$',views.delete_student_leave,name='permission_delete'),

    url(r'^vacation_add/$',views.add_vacation,name='vacation_add'),
    url(r'^vacation_table/(?P<personal_id>[0-9]*)$',views.table_vacation,name='vacation_table'),
    url(r'^vacation_delete/(?P<vacation_id>[0-9]+)$',views.delete_vacation,name='vacation_delete'),
    url(r'^vacation_edit/(?P<vacation_id>[0-9]+)$',views.edit_vacation,name='vacation_edit'),

    url(r'^attendance_add/$', views.add_attendance, name='attendance'),
    url(r'^attendance_table/$', views.table_attendance, name='attendance_table'),

    url(r'^mail_send/((?P<person_mail>\w+@\w+\.(com|net|org|biz|com\.tr|ru),)*)$',views.send_a_mail,name='send_collective_mail'),
    url(r'^change_position/(?P<student_id>[0-9]+)$',views.change_student_position,name='change_position'),
    url(r'^create_egm_xml/$',views.create_egm_xml,name='create_egm_xml'),

]