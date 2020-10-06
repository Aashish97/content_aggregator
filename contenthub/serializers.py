from rest_framework import serializers
from .models import Content
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


'''
    UserSerializer allows creating of the user
    user.set_password ensures that we set password correctly, rather than setting the raw password as the hash.
    extra_kwargs = {'password': {'write_only': True}} ensures user dont get back the password in response.
    Token.objects.create(user=user) creates a unique token for every users so that token can be used for identifying the user
'''

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

'''
    ContentSerializer serializes the all field of Content model instances into API format i.e, json format
'''


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
