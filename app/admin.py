# from django.contrib import admin

# from .models import Character

# admin.site.register(Character)

from django.contrib import admin

from .models import Character

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_occupation_display', 'description')  
    search_fields = ('name', 'occupation')  
    list_filter = ('occupation',)  
    list_editable = ('description',)  

admin.site.register(Character, CharacterAdmin)

