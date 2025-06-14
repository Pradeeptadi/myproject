from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/', views.page, name='page'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]
