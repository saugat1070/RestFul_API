from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
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


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    desc = models.CharField(max_length=100)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE,related_name='reviews')
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.rating} {self.watchlist.title}'
    
    