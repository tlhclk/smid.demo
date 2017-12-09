# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views,forms

app_name='user_panel'
urlpatterns = [
    url(r'^user_add/$', views.add_user, name='Registration'), #TODO: veri tabanıotamamen oturduktann sonra bu fonksiyon ve urller kalıcak veya sislinecek
    url(r'^user/(?P<user_id>[0-9]+)$', views.detail_user, name='User Details'),
    url(r'^user_table/$', views.table_user, name='User Table'),
    url(r'^user_edit/(?P<user_id>[0-9]+)$',views.edit_user,name='User Edit'),
    url(r'^user_delete/(?P<user_id>[0-9]+)$',views.delete_user ,name='User Delete'),
    url(r'^login/$',views.log_in,name='login'),
    url(r'^logout/$',views.log_out,name='logout'),
    url(r'^register/$',views.register,name='register'),
    #url(r'^group/(?P<group_id>[0-9]+)/', views.detail_group, name='Group Detail'),
    #url(r'^group_table/',views.table_group ,name='Group Table'),
    #url(r'^permission_table/',views.table_permission ,name='Permission Table'),
    #url(r'^permission_add/',views.permission_add,name='Permission add'),
    #url(r'^group_permission_add/',views.group_permission_add,name='asd'),
    #url(r'^add_group/',views.add_group,name='qwe'),
    url(r'^company_add/$',views.add_company,name=''),
    url(r'^company_detail/(?P<company_id>[0-9]+)$',views.detail_company,name=''),
    url(r'^company_table/$',views.table_company,name=''),
    url(r'^company_edit/(?P<company_id>[0-9]+)$',views.edit_company,name=''),
    url(r'^company_delete/(?P<company_id>[0-9]+)$',views.delete_company,name=''),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name':'registration/password_reset_form.html',
                                                        'email_template_name':'registration/password_reset_email.html',
                                                        'subject_template_name':'registration/password_reset_subject.txt',
                                                        'post_reset_redirect':'user_panel:password_reset_done',
                                                        'extra_context':{'title':'Şifre Sıfırlama'}},name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name':'registration/password_reset_form.html',
                                                        'extra_context':{'title':'Şifre Sıfırlama'}},name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,{'template_name':'registration/password_reset_confirm.html',
                                                        'post_reset_redirect':'user_panel:password_reset_complete',
                                                        'extra_context':{'title':'Şifre Sıfırlama'}}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,{'template_name':'registration/password_reset_complete.html',
                                                        'extra_context':{'title':'Şifre Sıfırlama'}}, name='password_reset_complete'),

]