# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('footballApp/', views.footballApp, name='footballApp'),
#     path('', views.footballApp, name='footballApp'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.footballApp, name='footballApp'),
]