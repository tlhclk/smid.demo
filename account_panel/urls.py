# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='account_panel'
urlpatterns = [
    url(r'^transaction_add/(?P<filter_no>[0-9]*)$', views.add_transaction, name='add_transaction'),
    url(r'^transaction_table/$', views.table_transaction, name='transaction_table'),
    url(r'^transaction_edit/(?P<transaction_no>[0-9]+)$', views.edit_transaction, name='transaction_edit'),
    url(r'^transaction_delete/(?P<transaction_no>[0-9]+)$', views.delete_transaction, name='transaction_delete'),

    url(r'^asset_add/$', views.add_asset, name='add_asset'),
    url(r'^asset/(?P<asset_no>[0-9]+)$', views.detail_asset, name='asset_details'),
    url(r'^asset_table/$', views.table_asset, name='asset_table'),
    url(r'^asset_edit/(?P<asset_no>[0-9]+)$', views.edit_asset, name='asset_edit'),
    url(r'^asset_delete/(?P<asset_no>[0-9]+)$', views.delete_asset, name='asset_delete'),

    url(r'^account_add/$', views.add_account, name='add_account'),
    url(r'^account/(?P<account_no>[0-9]+)$', views.detail_account, name='account_details'),
    url(r'^account_table/$', views.table_account, name='account_table'),
    url(r'^account_edit/(?P<account_no>[0-9]+)$', views.edit_account, name='account_edit'),
    url(r'^account_delete/(?P<account_no>[0-9]+)$', views.delete_account, name='account_delete'),

    url(r'^bill_add/$', views.add_bill, name='add_bill'),
    url(r'^bill/(?P<bill_no>[0-9]+)$', views.detail_bill, name='bill_details'),
    url(r'^bill_table/$', views.table_bill, name='bill_table'),
    url(r'^bill_edit/(?P<bill_no>[0-9]+)$', views.edit_bill, name='bill_edit'),
    url(r'^bill_delete/(?P<bill_no>[0-9]+)$', views.delete_bill, name='bill_delete'),

    url(r'^periodic_payment/(?P<month>[0-9]*)$',views.periodic_payment,name='periodic_payment')
]