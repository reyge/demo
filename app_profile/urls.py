# from django.contrib import admin
from django.urls import path, include
from . import views
from . import views_admin

urlpatterns = [
    path('register/', views_admin.registerPage, name="register"),
    path('login/', views_admin.loginPage, name="login"),
    path('logout/', views_admin.logoutUser, name="logout"),

    path('', views.home, name='home'),
    path('ad/', views_admin.dashboard, name='dashboard'),
    path('info/', views_admin.info, name='info'),
    path('language/', views_admin.language, name='language'),
    path('interest/', views_admin.interest, name='interest'),
    path('experience/', views_admin.experience, name='experience'),

    path('education/', views_admin.education, name='education'),
    path('update_education/<int:id>', views_admin.education, name="update_education"),

]