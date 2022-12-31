from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request: HttpRequest):
    SEARCH_COMPONENT: str = 'search-movie'

    search_term: str = request.GET.get(SEARCH_COMPONENT)
    return render(request, 'home.html', {
        'search_term': search_term
    })

def about(request: HttpRequest):
    return HttpResponse('<h1>Welcome to the About page</h1>')

def signup(request: HttpRequest):
    EMAIL_COMPONENT = 'email'

    email = request.GET.get(EMAIL_COMPONENT)
    return render(request, 'signup.html', {
        'email': email
    })