# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='user_panel'
urlpatterns = [
    url(r'^$', views.option_menu, name='user-group-permission Option Menu'),
    url(r'^user_add/', views.add_user, name='Registration'),
    url(r'^user/(?P<user_id>[0-9]+)/', views.detail_user, name='User Details'),
    url(r'^user_table/', views.table_user, name='User Table'),
    url(r'^user_edit/(?P<user_id>[0-9]+)/',views.edit_user,name='User Edit'),
    url(r'^user_delete/(?P<user_id>[0-9]+)/',views.delete_user ,name='User Delete'),
    url(r'^login/',views.log_in,name='Log in'),
    url(r'^logout/',views.log_out,name='Log out'),
    url(r'^group/(?P<group_id>[0-9]+)/', views.detail_group, name='Group Detail'),
    url(r'^group_table/',views.table_group ,name='Group Table'),
    url(r'^permission_table/',views.table_permission ,name='Permission Table'),
    url(r'^permission_add/',views.permission_add,name='Permission add'),
    url(r'^group_permission_add/',views.group_permission_add,name='asd'),
    url(r'^add_group/',views.add_group,name='qwe'),
    url(r'^company_add/',views.add_company,name=''),
    url(r'^company_detail/(?P<company_id>[0-9]+)',views.detail_company,name=''),
    url(r'^company_table/',views.table_company,name=''),
    url(r'^company_edit/(?P<company_id>[0-9]+)',views.edit_company,name=''),
    url(r'^company_delete/(?P<company_id>[0-9]+)',views.delete_company,name=''),

]