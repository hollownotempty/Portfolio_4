from django.urls import path
from . import views

urlpatterns = [
    path('', views.returnHome, name='home'),
    path('submit/', views.submit_page, name='submit'),
    path('about/', views.returnAboutPage, name='about'),
    path('submissions', views.return_appointments, name='submissions'),
    path('delete_submission/<submission_id>', views.delete_submission, name='delete_submission'),
]
