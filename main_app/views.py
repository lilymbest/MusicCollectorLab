from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Music

# Add the following import
from django.http import HttpResponse

# Define the home view
class MusicCreate(CreateView):
    model = Music
    fields = ['name', 'artist', 'album']
    success_url = '/'

class MusicDelete(DeleteView):
    model = Music
    success_url = '/'

class MusicUpdate(UpdateView):
    model = Music
    fields = ['name', 'artist', 'album']
    success_url = '/'

def home(request):
    return render(request, 'home.html')

def music_details(request, music_id):
    music = Music.objects.get(id=music_id)
    return render(request, 'main_app/music_detail.html', {'music': music})
