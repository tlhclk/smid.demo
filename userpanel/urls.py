# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='user_panel'
urlpatterns = [
    url(r'^$', views.options_menu, name='user-group-permission Option Menu'),
    url(r'^registration', views.user_add, name='Registration'),
    url(r'^user/(?P<user_id>[0-9]+)/', views.user_detail, name='User Details'),
    url(r'^user_table/', views.user_table, name='User Table'),
    url(r'^user_delete/(?P<user_id>[0-9]+)/',views.user_delete ,name='User Delete'),
    url(r'^login/',views.log_in,name='Log in'),
    url(r'^logout/',views.log_out,name='Log out'),
    url(r'^remover/', views.remover, name='remover'),
    url(r'^group/(?P<group_id>[0-9]+)/', views.group_detail, name='Group Detail'),
    url(r'^group_table/',views.group_table ,name='Group Table'),
    url(r'^group_delete/(?P<group_id>[0-9]+)/',views.group_delete ,name='Group Delete'),
    url(r'^permission_add/',views.permission_add ,name='Permission Add'),
    url(r'^permission_table/',views.permission_table ,name='Permission Table'),
    url(r'^permission_delete/(?P<permission_id>[0-9]+)/',views.permission_delete ,name='Permission Delete'),
    url(r'^user_permission_add/',views.user_permission_add ,name='User Permission Add'),
    url(r'^group_permission_add',views.group_permission_add ,name='Group Permission Add'),
]