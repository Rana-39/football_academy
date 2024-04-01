from django.urls import path
from . import views

# urlpatterns = [
#     path('members/', views.members, name='members'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catapp, name='members'),
    path('AppBar/', views.review, name='AppBar'),
]