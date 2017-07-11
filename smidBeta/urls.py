from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_page,name='home page'),
    url(r'^account_panel/',include('account_panel.urls')),
    url(r'^calendar_panel/',include('calendar_panel.urls')),
    url(r'^document_panel/',include('document_panel.urls')),
    url(r'^operation_panel/',include('operation_panel.urls')),
    url(r'^person_panel/',include('person_panel.urls')),
    url(r'^stock_panel/',include('stock_panel.urls')),
    url(r'^user_panel/',include('user_panel.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
