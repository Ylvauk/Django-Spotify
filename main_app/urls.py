from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
        path('songs/', views.SongList.as_view(), name='song-list'),
    
]