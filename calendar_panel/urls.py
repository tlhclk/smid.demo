# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'calendar_panel'
urlpatterns = [
    url(r'^event/add$', views.event_add, name='event_add'),
    url(r'^event/detail/(?P<event_id>.*)$', views.event_detail, name='event_detail'),
    url(r'^event/edit/(?P<event_id>.*)$', views.event_edit, name='event_edit'),
    url(r'^event/delete/(?P<event_id>.*)$', views.event_delete, name='event_delete'),

    url(r'^birthday_calendar/$', views.birthday_calendar, name='birthday_calendar'),
    url(r'^agenda/$', views.agenda, name='agenda'),
    url(r'^calendar/$', views.event_calendar, name='calendar'),

]
