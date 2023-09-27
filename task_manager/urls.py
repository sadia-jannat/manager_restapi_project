"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from unicodedata import name


# task_app to use views add
from task_app import views
#image add ar jonno
from django.conf import settings
from django.conf.urls.static import static


#API
from task_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="index" ),
    path('registration/', views.registration, name="registration" ),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('task_creation/', views.task_creation, name="task_creation"),
    path('task_list/', views.task_list, name='task_list'),
    path('task_list_edit/<int:id>/', views.task_list_edit, name='task_list_edit'),
    path('task_list_delete/<int:id>/', views.task_list_delete, name='task_list_delete'),
    path('task_search/', views.task_search, name="task_search"),

    path('', include('task_app.urls')),
    

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
