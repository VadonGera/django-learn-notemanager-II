from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UserModelTest(TestCase):
    """    Тест модели User    """

    # Инит начальных данных для теста
    # Создаем пользователя с правами администратора
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@mail.ru',
            password='123456',
            first_name='first_name',
            last_name='last_name',
            is_admin=True,
            is_active=True,
        )

    # Проверяем создание обычного пользователя
    def test_create_user(self):
        user_second = User.objects.create_user(
            email='second@mail.ru',
            password='123456',
            first_name='first_name_second',
            last_name='last_name_second',
        )
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(user_second.first_name, 'first_name_second')

        user_second.delete()
        self.assertEqual(User.objects.count(), 1)
