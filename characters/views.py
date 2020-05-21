from django.shortcuts import render, redirect
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
    characters = Character.objects.filter(user_id=user.id, banned='No')
    return render(request, 'characters.html', {'characters': characters})


@login_required()
def set_main_character(request):
    """
    a view to bring up all the users's characters and set one as the main one
    """
    user = User.objects.get(id=request.user.id)
    characters = Character.objects.filter(user_id=user.id, banned='No')
    return render(request, 'set_main_character.html', {'characters': characters})


@login_required()
def set_main_char_post(request):
    """
    sets main character within the list
    """
    user = User.objects.get(id=request.user.id)
    characters = Character.objects.filter(user_id=user.id, banned='No')
    characters.update(main_character="No")

    selected_char = Character.objects.filter(id=request.POST.get('charSelector'))
    selected_char.update(main_character="Yes")

    return redirect(view_characters)

@login_required()
def delete_character(request, id):
    """
    Deletes the character and redirects to the character screen
    """

    character = Character.objects.filter(id=id).first()
    character.delete()

    return redirect(view_characters)