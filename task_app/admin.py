from django.contrib import admin

# Register your models here.
from .models import TaskModel
@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display= ('title', 'description', 'due_date', 'photo', 'option_priority', 'task_complete', 'create_time')
                    


