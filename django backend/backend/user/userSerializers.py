from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    name = SerializerMethodField()
    email = SerializerMethodField()

    def get_email(self, object):
        return object.username

    def get_name(self, object):
        return object.first_name

    class Meta:
        model = User
        fields = ["name", "email"]
