from django.urls import path

from main.views import HomeView, get_all_departments

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('get_all_departments', get_all_departments, name='get_all_departments')
]
