from django.conf.urls import url
from . import views

app_name='stock_panel'
urlpatterns = [
    url(r'^$',views.option_menu,name='Fixture-Room-Liability Option Menu'),
    url(r'^fixture_add/', views.add_fixture, name='Add Fixture to a Room'),
    url(r'^fixture/(?P<fixture_no>[0-9]+)/', views.fixture_detail, name='Fixture Details'),
    url(r'^fixture_table/', views.table_fixture, name='Fixture Table'),
    url(r'^fixture_edit/(?P<fixture_no>[0-9]+)/', views.edit_fixture, name='Fixture Edit'),
    url(r'^fixture_delete/(?P<fixture_no>[0-9]+)/',views.delete_fixture,name='Fixture Delete'),
    url(r'^room_add/', views.add_room, name='Add room to a Room'),
    url(r'^room/(?P<room_no>[0-9]+)/', views.room_detail, name='Room Details'),
    url(r'^room_table/', views.table_room, name='room Table'),
    url(r'^room_edit/(?P<room_no>[0-9]+)/', views.edit_room, name='room Edit'),
    url(r'^room_delete/(?P<room_no>[0-9]+)/',views.delete_room,name='Room Delete'),
    url(r'^liability_add/',views.liability_add,name='Liability Add'),
    url(r'^liability/(?P<record_no>[0-9]+)', views.liability_detail, name='Liability detail'),
    url(r'^liability_table/',views.liability_table,name='Liability Table'),
    url(r'^liability_edit/(?P<record_no>[0-9]+)', views.liability_edit, name='Liability Edit'),
    url(r'^liability_delete/(?P<record_no>[0-9]+)', views.liability_delete, name='Liability delete'),
]