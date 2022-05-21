from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_user', views.show_user_form, name='show_user_form'),
    path('add_event', views.show_event_form, name='show_event_form'),
    path('add_squad', views.show_squad_form, name='show_squad_form'),
    path('add_camp', views.show_camp_form, name='show_camp_form'),
]
