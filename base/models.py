from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class movieimg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')

class aboutmovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ManyToManyField(movieimg, related_name="image")
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    genre = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    link = models.URLField(max_length=300, null=True)
    done = models.BooleanField(default=False)

class review(models.Model):
    join = models.ForeignKey(aboutmovie, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True)