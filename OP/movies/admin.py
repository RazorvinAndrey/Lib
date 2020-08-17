from django.contrib import admin

# Register your models here.
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStars, Reviews


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStars)
admin.site.register(Reviews)

