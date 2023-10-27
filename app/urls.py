from django.urls import path
from .views import character_list

urlpatterns = [
    path('characters/', character_list, name='character-list'),
]