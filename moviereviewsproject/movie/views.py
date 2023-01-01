from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.db.models.query import QuerySet
from django.contrib.auth.decorators import login_required

from .models import Movie, Review
from .forms import ReviewForm

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
    reviews = Review.objects.filter(movie = movie)
    return render(request, 'detail.html', {
        'movie': movie,
        'reviews': reviews
    })

@login_required
def create_review(request: HttpResponse, movie_id: int):
    movie = get_object_or_404(Movie, pk=movie_id)
    if (request.method == 'GET'):
        return render(request, 'create-review.html', {
            'form': ReviewForm,
            'movie': movie
        })
    else:
        try:
            form = ReviewForm(request.POST)
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.movie = movie
            new_review.save()
            return redirect('detail', new_review.movie.id)
        except ValueError:
            return render(request, 'create-review.html', {
                'form': ReviewForm,
                'error': 'Invalid data entered - please retry'
            })

@login_required
def update_review(request: HttpResponse, review_id: int):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    
    if (request.method == 'GET'):
        form = ReviewForm(instance=review)
        return render(request, 'update-review.html', {
            'review': review,
            'form': form
        })
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie_id)
        except ValueError:
            return render(request, 'update-review.html', {
                'review': review,
                'form': form,
                'error': 'Invalid data entered - please retry'
            })

@login_required
def delete_review(request: HttpResponse, review_id: int):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)