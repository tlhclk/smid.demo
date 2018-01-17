# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='document_panel'
urlpatterns = [
    url(r'^document_add/$',views.add_document,name='document_add'),
    url(r'^document/(?P<document_id>[0-9]+)$',views.document_detail,name='document_details'),
    url(r'^document_table/(?P<student_id>[0-9]*)$',views.table_document,name='document_table'),
    url(r'^document_edit/(?P<document_id>[0-9]+)$',views.edit_document,name='document_edit'),
    url(r'^document_delete/(?P<document_id>[0-9]+)$',views.delete_document,name='document_delete'),

    url(r'^liability_add/$',views.liability_add,name='liability_add'),
    url(r'^liability/(?P<record_no>[0-9]+)$', views.liability_detail, name='liability_detail'),
    url(r'^liability_table/(?P<student_id>[0-9]*)$',views.liability_table,name='liability_table'),
    url(r'^liability_edit/(?P<record_no>[0-9]+)$', views.liability_edit, name='liability_edit'),
    url(r'^liability_delete/(?P<record_no>[0-9]+)$', views.liability_delete, name='liability_delete'),
]