from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('handle_emoji_click/', views.handle_emoji_click, name='handle_emoji_click'),
    path('emoji_percentage/', views.emoji_percentage, name='emoji_percentage'),
]