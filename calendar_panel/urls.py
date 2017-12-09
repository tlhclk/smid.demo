# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='calendar_panel'
urlpatterns = [
    url(r'^birthday_calendar/$',views.birthday_calendar,name='Doğum Günü Takvimi'),
    url(r'^graph_demo/$',views.graph,name='Graph Demo'),
    url(r'^calendar/$',views.calendar,name='calendar')
]