from django.contrib.auth.models import User
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import authenticate

from .models import *


class ProfileSerializer(serializers.Serializer):
    bio = serializers.CharField()
    birth_date = serializers.DateField()
    country = serializers.CharField()
    job = serializers.CharField()


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class UserSerializer(UserDetailsSerializer):
    profile = ProfileSerializer(required=False)
    settings = SettingsSerializer(required=False)

    class Meta(UserDetailsSerializer.Meta):
        fields = (
                'id', 'username', 'email', 'first_name', 'last_name', 'profile', 'settings'
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        bio = profile_data.get('bio')
        birth_date = profile_data.get('birth_date')
        country = profile_data.get('country')
        job = profile_data.get('job')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data:
            profile.bio = bio
            profile.birth_date = birth_date
            profile.country = country
            profile.job = job
            profile.save()
        return instance

# Register Serializer

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        user_profile = Profile.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials Or Account is not active.")


# class PasswordChangeSerializer(PasswordChangeSerializer):
#     set_password_form_class = SetPasswordForm