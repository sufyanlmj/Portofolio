from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('daftar/', views.daftar, name='daftar'),
    
    path('', views.about, name='about'),
    path('about_create/', views.about_create, name='about_create'),
    path('about_update/<int:pk>/', views.about_update, name='about_update'),
    path('about_delete/<int:pk>/', views.about_delete, name='about_delete'),

    path('profile/', views.profile, name='profile'),
    path('profile_create/', views.profile_create, name='profile_create'),
    path('profile_update/<int:pk>/', views.profile_update, name='profile_update'),
    path('profile_delete/<int:pk>/', views.profile_delete, name='profile_delete'),

    path('sertifikat/', views.sertifikat, name='sertifikat'),
    path('sertifikat_create/', views.sertifikat_create, name='sertifikat_create'),
    path('sertifikat_update/<int:pk>/', views.sertifikat_update, name='sertifikat_update'),
    path('sertifikat_delete/<int:pk>/', views.sertifikat_delete, name='sertifikat_delete'),

    path('project/', views.project, name='project'),
    path('project_create/', views.project_create, name='project_create'),
    path('project_update/<int:pk>/', views.project_update, name='project_update'),    
    path('project_delete/<int:pk>/', views.project_delete, name='project_delete'),

    path('design/', views.design, name='design'),
    path('design_create/', views.design_create, name='design_create'),
    path('design_update/<int:pk>/', views.design_update, name='design_update'),
    path('design_delete/<int:pk>/', views.design_delete, name='design_delete'),

    path('skills/', views.skills, name='skills'),
]