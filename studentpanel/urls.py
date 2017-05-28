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
    url(r'^parent_table/',views.table_parent,name='Parent List'),
    url(r'^parent/(?P<parent_id>[0-9]+)/', views.detail_parent, name='parent Details'),
    url(r'^parent_table/', views.table_parent, name='parent Table'),
    url(r'^parent_edit/(?P<parent_id>[0-9]+)', views.edit_parent, name='parent Edit'),
    url(r'^parent_delete/(?P<parent_id>[0-9]+)', views.delete_parent, name='parent Delete'),

]