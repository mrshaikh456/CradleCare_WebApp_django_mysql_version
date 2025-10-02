# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Core
    path('', views.dashboard, name='dashboard'), 
    path('add_baby/', views.add_baby, name='add_baby'),
    
    # General Features
    path('recipes/', views.recipe_book, name='recipe_book'),
    path('journal/', views.personal_journal, name='personal_journal'),
    
    # Baby Specific URLs
    path('baby/<int:baby_id>/', views.baby_detail, name='baby_detail'), 
    path('baby/<int:baby_id>/growth/', views.growth_tracker, name='growth_tracker'),
    path('baby/<int:baby_id>/sleep/', views.sleep_tracker, name='sleep_tracker'),
    path('baby/<int:baby_id>/feeding/', views.feeding_tracker, name='feeding_tracker'),
    path('baby/<int:baby_id>/appointments/', views.appointment_tracker, name='appointment_tracker'),
    path('baby/<int:baby_id>/milestones/', views.milestone_tracker, name='milestone_tracker'),
    path('baby/<int:baby_id>/vaccinations/', views.vaccination_schedule, name='vaccination_schedule'),

    # Delete URLs
    path('growth/delete/<int:log_id>/', views.delete_growth_log, name='delete_growth_log'),
    path('sleep/delete/<int:log_id>/', views.delete_sleep_log, name='delete_sleep_log'),
    path('feeding/delete/<int:log_id>/', views.delete_feeding_log, name='delete_feeding_log'),
    path('appointment/delete/<int:log_id>/', views.delete_appointment, name='delete_appointment'),
    path('milestone/delete/<int:log_id>/', views.delete_milestone, name='delete_milestone'),
]