from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'data_nascimento', 'telefone', 'cpf','id')


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', 'email',
                  'first_name', 'last_name', 'data_nascimento', 'telefone', 'cpf')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        instance.username = validated_data.get('email', instance.email)
        return super(UserCreateSerializer, self).update(instance, validated_data)        
