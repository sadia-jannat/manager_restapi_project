from rest_framework import serializers
from task_app.models import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'due_date', 'photo', 'option_priority', 'task_complete', 'create_time']


