from django.conf.urls import url
from . import views,apps

app_name='account_panel'
urlpatterns = [
    url(r'^$', views.options_menu, name='Account Option Menu'),
    url(r'^transaction_add', views.add_transaction, name='Add transaction'),
    url(r'^transaction/(?P<transaction_no>[0-9]+)/', views.detail_transaction, name='transaction Details'),
    url(r'^transaction_table/', views.table_transaction, name='transaction Table'),
    url(r'^transaction_edit/(?P<transaction_no>[0-9]+)', views.edit_transaction, name='transaction Edit'),
    url(r'^transaction_delete/(?P<transaction_no>[0-9]+)', views.delete_transaction, name='transaction Delete'),
    url(r'^asset_add', views.add_asset, name='Add asset'),
    url(r'^asset/(?P<asset_no>[0-9]+)/', views.detail_asset, name='asset Details'),
    url(r'^asset_table/', views.table_asset, name='asset Table'),
    url(r'^asset_edit/(?P<asset_no>[0-9]+)', views.edit_asset, name='asset Edit'),
    url(r'^asset_delete/(?P<asset_no>[0-9]+)', views.delete_asset, name='asset Delete'),
    url(r'^account_add', views.add_account, name='Add account'),
    url(r'^account/(?P<account_no>[0-9]+)/', views.detail_account, name='account Details'),
    url(r'^account_table/', views.table_account, name='account Table'),
    url(r'^account_edit/(?P<account_no>[0-9]+)', views.edit_account, name='account Edit'),
    url(r'^account_delete/(?P<account_no>[0-9]+)', views.delete_account, name='account Delete'),
    url(r'^bill_add', views.add_bill, name='Add bill'),
    url(r'^bill/(?P<bill_no>[0-9]+)/', views.detail_bill, name='bill Details'),
    url(r'^bill_table/', views.table_bill, name='bill Table'),
    url(r'^bill_edit/(?P<bill_no>[0-9]+)', views.edit_bill, name='bill Edit'),
    url(r'^bill_delete/(?P<bill_no>[0-9]+)', views.delete_bill, name='bill Delete'),
]