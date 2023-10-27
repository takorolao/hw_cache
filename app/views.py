from django.shortcuts import render
from .models import Character
from django.core.cache import cache

def character_list(request):
    characters = cache.get('characters')
    if characters is None:
        characters = Character.objects.all()
        cache.set('characters', characters, 120)  
    return render(request, 'character_list.html', {'characters': characters})
