from django.urls import path

from . import views

# Original URL pattern: signupaccount/, which is not great.
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout_user'),
    path('login/', views.login_user, name='login_user')
]