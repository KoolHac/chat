from time import time
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='chat_url'),
    path('<str:chat>/<str:user>', views.chat_view, name='chat_view_url'),
    path('<str:chat>/<str:user>/read', views.read_message, name='get_url' ),
    path('<str:chat>/<str:user>/post/', views.post_message, name='post_url'),
    path('time/get/', views.get_time, name='time_url')
]