from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_songs, name='show_songs'),
    path('add/', views.add_song, name='add_song'),
    path('delete/<str:artist_name>/<str:title>/', views.delete_song, name='delete_song'),
]
