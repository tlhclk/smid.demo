from django.conf.urls import include, url
from django.conf.urls import (handler400, handler403, handler404, handler500)
from django.conf.urls.static import static,serve
from django.conf import settings
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
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

]
if  not settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
                    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), ]
else:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404='smidBeta.views.page_not404_found'
handler403='smidBeta.views.page_not403_found'
handler400='smidBeta.views.page_not400_found'
handler500='smidBeta.views.page_not400_found'