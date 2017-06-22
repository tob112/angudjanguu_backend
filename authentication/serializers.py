from rest_framework import serializers
from authentication.models import User
from django.contrib.auth import update_session_auth_hash


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'confirm_password')

        read_only_fields = ('created_at', 'updated_at')


        #
        # def create(self, validated_data):
        #     return User.objects.create(**validated_data)
        #
        # def update(self, instance, validated_data):
        #     instance.email = validated_data.get('email', instance.email)
        #
        #     instance.save()
        #
        #     password = validated_data.get('password', None)
        #     confirm_password = validated_data.get('confirm_password', None)
        #
        #     if password and confirm_password == confirm_password:
        #         instance.set_password(password)
        #         instance.save()
        #
        #     update_session_auth_hash(self.context.get('request'), instance)
        #
        #     return instance
