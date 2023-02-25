from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('entry_form/', views.add_entry, name='entry_form'),
    path('logout/', views.logout_user, name='logout'),
    path('entry/', views.view_entry, name='entry'),
]