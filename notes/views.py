from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Note
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
        # return Note.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


def note_list(request):
    all_notes = Note.objects.all()
    paginator = Paginator(all_notes, 4)
    page_number = request.GET.get('page')
    try:
        notes = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number не целое число, то выдать первую страницу
        notes = paginator.page(1)
    except EmptyPage:
        # Если page_number находится вне диапазона, то выдать последнюю страницу результатов
        notes = paginator.page(paginator.num_pages)

    return render(request, 'notes/list.html', {'notes': notes})


def note_item(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'notes/detail.html', {'note': note})

