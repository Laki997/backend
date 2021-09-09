from rest_framework import serializers
from src.users.models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, password):
        user = self.context['request'].user
        validate_password(password, user=user)
        return password

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
