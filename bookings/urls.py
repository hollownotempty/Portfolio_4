from django.urls import path
from . import views

urlpatterns = [
    path('', views.returnHome, name='home'),
    path('booking/', views.returnBookingPage, name='booking'),
    path('about/', views.returnAboutPage, name='about'),
    path('appointments', views.return_appointments, name='appointments'),
]
