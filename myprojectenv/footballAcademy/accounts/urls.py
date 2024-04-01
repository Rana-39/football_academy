from django.urls import path
from .views import SignUpView, profile, listOfPlayers
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('listOfPlayers/', views.listOfPlayers, name='listOfPlayers'),
]
