from django.contrib.auth import views
from django.urls import path
from .views import view_characters, set_main_character, set_main_char_post, delete_character, create_new_character


urlpatterns = [
    path('view/', view_characters, name="view_characters"),
    path('set_main_char/', set_main_character, name="set_main_character"),
    path('set_main_char_post/', set_main_char_post, name="set_main_char_post"),
    path('delete_char/<int:id>', delete_character, name="delete_character"),
    path('new_char/', create_new_character, name="create_new_character")
]