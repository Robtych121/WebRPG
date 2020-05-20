from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Character


# Create your views here.
@login_required()
def view_characters(request):
    """
    a view to bring up the user's available characters
    """
    user = User.objects.get(id=request.user.id)
    characters = Character.objects.filter(user_id=user.id)
    return render(request, 'characters.html', {'characters': characters})