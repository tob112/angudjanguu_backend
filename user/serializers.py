from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'groups')

        # def update(self, instance, validated_data):
        #     instance.username = validated_data.get('username', instance.username)
        #     instance.email = validated_data.get('email', instance.email)
        #
        #     instance.save()
