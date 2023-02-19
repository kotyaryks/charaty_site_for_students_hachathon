from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('team/', views.team, name='team'),
    path('shelters/', views.shelters, name='shelters'),
    path('reports/', views.reports, name='reports'),
]
