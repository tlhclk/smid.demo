# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='document_panel'
urlpatterns = [
    url(r'^option_menu/',views.option_menu,name='Document Option Menu'),
    url(r'^document_add/',views.add_document,name='Document Add'),
    url(r'^document/(?P<document_id>[0-9]+)/',views.document_detail,name='Document Add'),
    url(r'^document_table/',views.table_document,name='Document Add'),
    url(r'^document_edit/(?P<document_id>[0-9]+)/',views.edit_document,name='Document Add'),
    url(r'^document_delete/(?P<document_id>[0-9]+)/',views.delete_document,name='Document Add'),
]