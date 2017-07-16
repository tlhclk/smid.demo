# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='person_panel'
urlpatterns = [
    url(r'^$', views.options_menu, name='Student-Parent Option Menu'),
    url(r'^student_id_add', views.add_student_id, name='Add Student ID'),
    url(r'^student_add', views.add_student, name='Add Student'),
    url(r'^student/(?P<student_id>[0-9]+)/', views.detail_student, name='Student Details'),
    url(r'^student_table/', views.table_student, name='Student Table'),
    url(r'^student_edit/(?P<student_id>[0-9]+)', views.edit_student, name='Student Edit'),
    url(r'^student_delete/(?P<student_id>[0-9]+)', views.delete_student, name='Student Delete'),
    url(r'^parent_add/',views.add_parent,name='Add Parent'),
    url(r'^parent/(?P<parent_id>[0-9]+)/', views.detail_parent, name='parent Details'),
    url(r'^parent_table/', views.table_parent, name='parent Table'),
    url(r'^parent_edit/(?P<parent_id>[0-9]+)', views.edit_parent, name='parent Edit'),
    url(r'^parent_delete/(?P<parent_id>[0-9]+)', views.delete_parent, name='parent Delete'),
    url(r'^personal_add/', views.add_personal, name='Add personal'),
    url(r'^personal/(?P<personal_id>[0-9]+)/', views.detail_personal, name='personal Details'),
    url(r'^personal_table/', views.table_personal, name='personal Table'),
    url(r'^personal_edit/(?P<personal_id>[0-9]+)', views.edit_personal, name='personal Edit'),
    url(r'^personal_delete/(?P<personal_id>[0-9]+)', views.delete_personal, name='personal Delete'),
    url(r'^multiple/',views.multiple_add,name='Multiple')
]