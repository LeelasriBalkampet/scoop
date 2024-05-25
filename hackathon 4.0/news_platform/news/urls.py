from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:id>/', views.event_detail, name='event_detail'),
    path('submit/', views.submission_form, name='submission_form'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<str:category>/', views.category_articles, name='category_articles'),
]
