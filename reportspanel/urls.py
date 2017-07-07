from django.conf.urls import url
from . import views

app_name='reports_panel'
urlpatterns = [
    url(r'^$',views.options_menu,name='Reports Option Menu'),
    url(r'^attendance/(?P<room_no>[0-9]*)-(?P<student_id>[0-9]*)',views.student_attendance,name='Attandance'),
    url(r'^capacity/(?P<room_no>[0-9]*)',views.dorm_capacity,name='capacity'),
    url(r'^room_plan/',views.room_plan,name='Room Plan'),
]