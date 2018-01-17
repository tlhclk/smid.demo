from django.conf.urls import url
from . import views

app_name='report_panel'
urlpatterns = [
    url(r'^attendance/(?P<room_id>[0-9]*)-(?P<student_id>[0-9]*)$',views.student_attendance,name='Attandance'),
    url(r'^capacity/(?P<room_id>[0-9]*)$',views.dorm_capacity,name='capacity'),
    url(r'^room_plan/$',views.room_plan,name='Room Plan'),
    url(r'^contact_table/$',views.contact_table,name='Contact Table'),
    url(r'^payment_info/$',views.unpaid_rate,name='Ödeme Bilgileri'),
    url(r'^account_amount/(?P<account_no>[0-9]*)$',views.account_graphs,name='Hesap Miktarı'),
    url(r'^attendance_table/(?P<room_no>[0-9]*)-(?P<student_id>[0-9]*)$',views.student_attendance,name='Yoklama Tablosu'),
    url(r'^monthly_flow/(?P<month>[0-9]*)$',views.monthly_flow,name='Aylık Akış'),
    url(r'^multiple_filtering/$',views.filter_form,name='Filter Form'),
    url(r'^salary_table/$',views.salary_table,name='Salary Table')
]