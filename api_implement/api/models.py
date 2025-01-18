from django.db import models

# Create your models here.
class PlatForm(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=30)
    
    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=100)
    platform = models.ForeignKey(PlatForm, on_delete=models.CASCADE, related_name='watch_related')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title
    