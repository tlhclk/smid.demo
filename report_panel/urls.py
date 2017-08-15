from django.conf.urls import url
from . import views

app_name='report_panel'
urlpatterns = [
    url(r'^attendance/(?P<room_no>[0-9]*)-(?P<student_id>[0-9]*)',views.student_attendance,name='Attandance'),
    url(r'^capacity/(?P<room_no>[0-9]*)',views.dorm_capacity,name='capacity'),
    url(r'^room_plan/',views.room_plan,name='Room Plan'),
    url(r'^contact_table/',views.contact_table,name='Contact Table'),
    url(r'^payment_info/',views.unpaid_rate,name='Ödeme Bilgileri'),
    url(r'^money_flow/(?P<account_no>[0-9]*)',views.money_flow,name='Para Akışı'),
    url(r'^account_amount/',views.account_amount,name='Hesap Miktarı'),
    url(r'^attendance_table/(?P<room_no>[0-9]*)-(?P<student_id>[0-9]*)',views.student_attendance,name='Yoklama Tablosu'),
    url(r'^monthly_flow/',views.monthly_flow,name='Aylık Akış')
]