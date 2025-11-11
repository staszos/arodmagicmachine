from django.urls import path
from .views import layout, main_donation_structure
from . import views




urlpatterns = [
    path('', views.layout, name='layout'),
    path('main_donation_structure', views.main_donation_structure, name='main_donation_structure'),
    path('arod_main_FAQ', views.arod_main_FAQ, name='arod_main_FAQ'),
    path('arod_main_role_tariff', views.arod_main_role_tariff, name='arod_main_role_tariff'),
    path('arod_main_mix_donat_1', views.arod_main_mix_donat_1, name='arod_main_mix_donat_1'),
    path('arod_main_other_services', views.arod_main_other_services, name='arod_main_other_services'),
    path('arod_main_race_donat', views.arod_main_race_donat, name='arod_main_race_donat'),
    path('arod_main_item_list_donat_1', views.arod_main_item_list_donat_1, name='arod_main_item_list_donat_1'),
    path('arod_main_team_list_donat_1', views.arod_main_team_list_donat_1, name='arod_main_team_list_donat_1'),
    path('arod_main_magic_list_donat_1', views.arod_main_magic_list_donat_1, name='arod_main_magic_list_donat_1'),

]



