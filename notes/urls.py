from django.urls import path
from . import views
from .apps import NotesConfig

app_name = NotesConfig.name

urlpatterns = [
    path('api/notes/', views.NoteList.as_view(), name='note_list'),
    path('api/notes/<int:pk>/', views.NoteItem.as_view(), name='note_item'),

    path('notes/', views.note_list, name='note_list'),
    path('notes/<int:id>/', views.note_item, name='note_item'),
]
