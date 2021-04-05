from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSZ(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'mobile', 'email')

class WorkSZ(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"

class BugSZ(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = "__all__"

class WorkNestedSZ(serializers.ModelSerializer):
    assignees = UserSZ(many=True, read_only=False)

    class Meta:
        model = Work
        fields = "__all__"

class BugNestedSZ(serializers.ModelSerializer):
    discovered_by = UserSZ(read_only=False)

    class Meta: 
        model = Bug
        fields = "__all__"