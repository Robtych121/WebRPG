from django.shortcuts import get_object_or_404
from .models import Character
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def main_character(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        selected_main_character = Character.objects.filter(user_id=user.id, banned='No', main_character='Yes').first()
        return { 'selected_main_character':selected_main_character }
    else:
        return ''