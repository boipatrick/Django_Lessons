from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True) # Automatically set the date when the post is created"
    banner = models.ImageField(default='fallback.png', blank=True)  # Image field for the banner
    def __str__(self):
        return self.title