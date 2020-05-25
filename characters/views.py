from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Character
from .forms import NewCharacterForm
from game_common.stat_rolls import racialSTRModifier, racialDEXModifier, racialCONModifier, racialINTModifier, racialWISModifier, racialCHAModifier, classStatRole

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
    rolledStats = classStatRole()
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
                if data.get('role') == 'Barbarian':
                    character.strength = rolledStats[0] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[2] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[1] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[3] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[4] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[5] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Bard':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[1] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[3] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[5] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[0] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Cleric':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[3] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[1] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[0] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[5] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Druid':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[3] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[1] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[0] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[5] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Fighter':
                    character.strength = rolledStats[0] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[2] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[1] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[3] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[4] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[5] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Monk':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[0] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[3] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[1] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[5] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Paladin':
                    character.strength = rolledStats[0] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[2] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[3] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[5] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[1] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Ranger':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[0] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[3] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[1] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[5] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Rogue':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[0] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[3] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[5] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[1] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Sorcerer':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[3] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[1] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[5] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[0] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Warlock':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[3] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[1] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[4] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[5] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[0] + int(racialCHAModifier(data.get('race')))
                if data.get('role') == 'Wizard':
                    character.strength = rolledStats[2] + int(racialSTRModifier(data.get('race')))
                    character.dexterity = rolledStats[3] + int(racialDEXModifier(data.get('race')))
                    character.constitution = rolledStats[1] + int(racialCONModifier(data.get('race')))
                    character.intelligence = rolledStats[0] + int(racialINTModifier(data.get('race')))
                    character.wisdom = rolledStats[4] + int(racialWISModifier(data.get('race')))
                    character.charisma = rolledStats[5] + int(racialCHAModifier(data.get('race')))
            character.save()
            return redirect(view_characters)
    else:
        form = NewCharacterForm(instance=character)
    return render(request, 'create_new_character.html', {'form': form})