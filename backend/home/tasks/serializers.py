from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Task
        fields = [
            'user',
            'pk',
            'title',
            'description',
            'done'
        ]