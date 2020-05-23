from django.contrib.auth import views
from django.urls import path
from .views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name="game_dashboard"),
]