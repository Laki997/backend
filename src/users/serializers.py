from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from src.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if len(data.get('password')) < 6:
            raise ValidationError('Password too short')
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
