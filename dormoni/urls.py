# -*- coding: utf-8 -*-
"""dormoni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static,serve
from . import views
from django.conf.urls import (handler400, handler403, handler404, handler500)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',views.home_page,name='home'),
    url(r'^$',views.main_page,name='Main Page'),
    url(r'^account_panel/',include('account_panel.urls',namespace='account_panel')),
    url(r'^calendar_panel/',include('calendar_panel.urls',namespace='calendar_panel')),
    url(r'^document_panel/',include('document_panel.urls',namespace='document_panel')),
    url(r'^operation_panel/',include('operation_panel.urls',namespace='operation_panel')),
    url(r'^person_panel/',include('person_panel.urls',namespace='person_panel')),
    url(r'^report_panel/',include('report_panel.urls',namespace='report_panel')),
    url(r'^stock_panel/',include('stock_panel.urls',namespace='stock_panel')),
    url(r'^user_panel/',include('user_panel.urls',namespace='user_panel')),
    url(r'^contract/$', views.contract,name='contract'),
    url(r'^term_of_use/$', views.termofuse,name='termofuse'),
    url(r'^media/(?P<path>.*)$', views.media_view, name='media_root'),
    url(r'^static/(?P<path>.*)$', views.static_view, name='static_root'),
]



# error tanımları
handler404='smidBeta.views.page_not404_found'
handler403='smidBeta.views.page_not403_found'
handler400='smidBeta.views.page_not400_found'
handler500='smidBeta.views.page_not400_found'