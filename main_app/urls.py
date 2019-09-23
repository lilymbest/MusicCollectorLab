from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/add/', views.MusicCreate.as_view(), name='music_create'),
    path('/update/', views.MusicUpdate.as_view(), name='music_update'),
    path('/<int:pk>/delete', views.MusicDelete.as_view(), name='music_delete'),
]