from django.urls import path
from . import views

urlpatterns = [
    path('', views.returnHome),
    path('booking/', views.returnBookingPage)
]