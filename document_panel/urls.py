# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='document_panel'
urlpatterns = [
    url(r'^document_add/',views.add_document,name='Document Add'),
    url(r'^document/(?P<document_id>[0-9]+)',views.document_detail,name='Document Add'),
    url(r'^document_table/',views.table_document,name='Document Add'),
    url(r'^document_edit/(?P<document_id>[0-9]+)',views.edit_document,name='Document Add'),
    url(r'^document_delete/(?P<document_id>[0-9]+)',views.delete_document,name='Document Add'),
    url(r'^liability_add/',views.liability_add,name='Liability Add'),
    url(r'^liability/(?P<record_no>[0-9]+)', views.liability_detail, name='Liability detail'),
    url(r'^liability_table/',views.liability_table,name='Liability Table'),
    url(r'^liability_edit/(?P<record_no>[0-9]+)', views.liability_edit, name='Liability Edit'),
    url(r'^liability_delete/(?P<record_no>[0-9]+)', views.liability_delete, name='Liability delete'),
]