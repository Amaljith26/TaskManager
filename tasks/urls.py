from django.urls import path
from .views import IndexPageView
from . import views

urlpatterns = [
    path('', views.task_manager, name='task_manager'),
    path('create-task/', views.create_task, name='create_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('Sign In/', views.Signuppage, name='signup'),
    path('Login/', views.Loginpage, name='login'),
    path('Logout/',views.Logoutpage, name='logout'),
    
]