from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_company, name='search_company'),
]
