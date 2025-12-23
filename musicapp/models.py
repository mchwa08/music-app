from django.db import models

# Create your models here.
class song(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='media/', null = True, blank=True)

    def __str__(self):
        return f"{self.cover_image}:{self.title} by {self.artist} - {self.genre}"
    
