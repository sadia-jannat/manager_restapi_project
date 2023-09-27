import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets
from django import forms

#models
from .models import *
#django form create kore bellow models and forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms




#here django create it's own model and forms
class Create(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2' ]


class TaskModelForm(forms.ModelForm):
    class Meta:
        model=TaskModel()
        fields=['title', 'description', 'due_date', 'photo', 'option_priority', 'task_complete', 'create_time']         