from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_page, name='submit'),
    path('about/', views.about_page, name='about'),
    path('submissions/', views.return_appointments, name='submissions'),
    path('delete_submission/<submission_id>/', views.delete_submission, name='delete_submission'),
    path('edit_submission/<submission_id>/', views.edit_submission, name='edit_submission'),
]
