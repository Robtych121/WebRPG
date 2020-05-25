from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Character
from .forms import NewCharacterForm
from game_common.stat_rolls import statRoll, racialSTRModifier, racialDEXModifier, racialCONModifier, racialINTModifier, racialWISModifier, racialCHAModifier

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

@login_required()
def create_new_character(request, pk=None):
    character = get_object_or_404(Character, pk=pk) if pk else None
    data = request.POST.copy()
    user_id = request.user.id
    if request.method == 'POST':
        form = NewCharacterForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.user_id = user_id
            if data.get('statMethodController') == 'Manual':
                character.strength = int(data.get('strength')) + int(racialSTRModifier(data.get('race')))
                character.dexterity = int(data.get('dexterity')) + int(racialDEXModifier(data.get('race')))
                character.constitution = int(data.get('constitution')) + int(racialCONModifier(data.get('race')))
                character.intelligence = int(data.get('intelligence')) + int(racialINTModifier(data.get('race')))
                character.wisdom = int(data.get('wisdom')) + int(racialWISModifier(data.get('race')))
                character.charisma = int(data.get('charisma')) + int(racialCHAModifier(data.get('race')))
            else:
                character.strength = statRoll() + int(racialSTRModifier(data.get('race')))
                character.dexterity = statRoll() + int(racialDEXModifier(data.get('race')))
                character.constitution = statRoll() + int(racialCONModifier(data.get('race')))
                character.intelligence = statRoll() + int(racialINTModifier(data.get('race')))
                character.wisdom = statRoll() + int(racialWISModifier(data.get('race')))
                character.charisma = statRoll() + int(racialCHAModifier(data.get('race')))
            character.save()
            return redirect(view_characters)
    else:
        form = NewCharacterForm(instance=character)
    return render(request, 'create_new_character.html', {'form': form})