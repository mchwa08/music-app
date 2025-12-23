from django.shortcuts import render,redirect
from .models import song
 
 # Create your views here.
def show_songs(request):
    songs = song.objects.all()
    return render(request, 'show_songs.html', {'songs': songs})



def add_song(request):
    if request.method == 'POST':
        artist = request.POST['artist']
        title = request.POST['title']
        genre = request.POST['genre']
        cover_image = request.FILES.GET['cover_image']
        song.objects.create(artist=artist, title=title, genre=genre, cover_image=cover_image)
        return redirect('show_songs')
    return render(request, 'add_song.html')


def delete_song(request, artist_name, title):
    try:
        # Find the song by artist name and title (case-insensitive)
        brain = song.objects.filter(artist__iexact=artist_name, title__iexact=title).first()

        if brain:
            brain.delete()
            return redirect('/')
        else:
            return render(request, 'not_found.html', {
                'artist': artist_name,
                'title': title
            })

    except Exception as e:
        return redirect('/')