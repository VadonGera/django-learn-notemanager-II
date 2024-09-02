from django.test import TestCase
from django.contrib.auth import get_user_model
# from rest_framework.test import APITestCase
# from rest_framework.authtoken.models import Token

from .models import Note

User = get_user_model()


class NoteModelTest(TestCase):
    """    Тест модели Note    """

    # Инит начальных данных для теста
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@mail.ru',
            password='123456',
            first_name='first_name',
            last_name='last_name',
        )
        self.note = Note.objects.create(
            title='Test Note',
            description='Test Description',
            user=self.user,
        )

    # Проверяем создание заметки
    def test_create_note(self):
        note = Note.objects.create(
            title='Second Note',
            description='Another Description',
            user=self.user,
        )
        self.assertEqual(Note.objects.count(), 2)
        self.assertEqual(note.title, 'Second Note')

    # Обновляем заметку и проверяем, что изменения занесены.
    def test_update_note(self):
        self.note.title = 'Updated Note'
        self.note.save()
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    # Удаляем заметку и проверяем, что ее больше нет
    def test_delete_note(self):
        self.note.delete()
        self.assertEqual(Note.objects.count(), 0)

    # Проверяем получения заметки
    def test_retrieve_note(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, 'Test Note')

