from django.conf.urls import url
from . import views

app_name='student_panel'
urlpatterns = [
    url(r'^$', views.options_menu, name='Student-Parent Option Menu'),
    url(r'^student_add', views.add_stundent, name='Add Student'),
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
    url(r'^change_position/(?P<student_id>[0-9]+)/',views.change_student_position,name='change student position'),
    url(r'^permission_assign/',views.leave_assign,name='Permission Assign')
]