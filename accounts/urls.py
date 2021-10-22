from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.returnLogin, name='login'),
    path('signup/', views.returnSignup, name='signup'),
]
