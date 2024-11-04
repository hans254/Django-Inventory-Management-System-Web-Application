from django.urls import path
from . import views

urlpatterns = [
    path('your-url-pattern/', views.dashboard, name='dashboard'),
    # Add more URL patterns as needed
]