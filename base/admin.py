from django.contrib import admin
from .models import movieimg, aboutmovie, review
# Register your models here.
admin.site.register(movieimg)
admin.site.register(aboutmovie)
admin.site.register(review)