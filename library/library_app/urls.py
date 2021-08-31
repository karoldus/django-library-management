from django.urls import path
from . import views #z obecnego katalogu

urlpatterns = [
    path('', views.home, name='home'),
]