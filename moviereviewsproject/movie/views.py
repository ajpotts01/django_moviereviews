from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.db.models.query import QuerySet

from .models import Movie

# Create your views here.
def home(request: HttpRequest):
    SEARCH_COMPONENT: str = 'search-movie'

    movies: QuerySet = None

    search_term: str = request.GET.get(SEARCH_COMPONENT)

    if (search_term):
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
        
    return render(request, 'home.html', {
        'search_term': search_term,
        'movies': movies
    })

def about(request: HttpRequest):
    return HttpResponse('<h1>Welcome to the About page</h1>')

def mailing_list(request: HttpRequest):
    EMAIL_COMPONENT = 'email'

    email = request.GET.get(EMAIL_COMPONENT)
    return render(request, 'mailing-list.html', {
        'email': email
    })

def detail(request: HttpRequest, movie_id: int):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {
        'movie': movie
    })