from django.contrib.auth import views
from django.urls import path
from .views import view_characters


urlpatterns = [
    path('view/', view_characters, name="view_characters")
]