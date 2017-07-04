from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page

urlpatterns = [
    url(r'^user_panel/', include('userpanel.urls')),
    url(r'^student_panel/', include('studentpanel.urls')),
    url(r'^fixture_panel/',include('fixturepanel.urls')),
    url(r'^reports_panel/',include('reportspanel.urls')),
    #url(r'^accountpanel/', include('accountpanel.urls')),
    url(r'^$',home_page,name='home page'),
    url(r'^admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
