from django.urls import path
from .views import *
urlpatterns = [
    path('app_advertisements/', index,  name ='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]