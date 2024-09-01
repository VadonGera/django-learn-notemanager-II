from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False) # Пароль не обязателен при обновлении

    def create(self, validated_data):
        # Создание нового пользователя
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=False,
            is_admin=False,
        )
        return user

    def update(self, instance, validated_data):
        # Обновление пользователя
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)

        # Проверка и обновление пароля
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin')

