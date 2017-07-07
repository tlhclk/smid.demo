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
    url(r'^permission_assign/',views.leave_assign,name='Permission Assign'),
    url(r'^send_collective_message',views.send_collective_message,name='Send Collective Mesaj'),
    url(r'^attendance_table',views.attendance_table,name='Attendance List'),
    url(r'^document_add/',views.add_document,name='Document Add'),
    url(r'^document/(?P<document_id>[0-9]+)/',views.document_detail,name='Document Add'),
    url(r'^document_table/',views.table_document,name='Document Add'),
    url(r'^document_edit/(?P<document_id>[0-9]+)/',views.edit_document,name='Document Add'),
    url(r'^document_delete/(?P<document_id>[0-9]+)/',views.delete_document,name='Document Add'),
    url(r'^entrance_leave/',views.add_entrance_leave,name='Entrance'),
    url(r'^entrance_leave_table/',views.entranceleave_table,name='Entrance Leave Table'),
    url(r'^liability_add/',views.liability_add,name='Liability Add'),
    url(r'^liability/(?P<record_no>[0-9]+)', views.liability_detail, name='Liability detail'),
    url(r'^liability_table/',views.liability_table,name='Liability Table'),
    url(r'^liability_edit/(?P<record_no>[0-9]+)', views.liability_edit, name='Liability Edit'),
    url(r'^liability_delete/(?P<record_no>[0-9]+)', views.liability_delete, name='Liability delete'),
    url(r'^contact_table/',views.contact_table,name='Contact Table')
]