from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from task_app import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse,json
from django.shortcuts import redirect
from django.contrib import messages
#query ar jonno
from django.db.models import Q
#from .forms import SearchForm

import json
#serializers work need
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from task_app.models import TaskModel
from task_app.serializers import TaskSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#requests-and-responses api serializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# all models and forms name add korar jonno * use kora jay
from .models import *
from .forms import *


#from django.contrib.auth.forms import UserCreationForm, authenticate all for registration process.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import Create
from django.contrib.auth.models import User


def index(request):

    form=Create()
    
    if request.method == "POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account create successfully!!')
            
    context={'form':form}  

    return render(request, 'index.html', context)

def registration(request):

     form=Create()
    
     if request.method == "POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account create successfully!!')
            
     context={'form':form}  

     return render(request, 'registration.html', context)


login_result=1
def userlogin(request):
    if request.method == "POST":       
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user=authenticate(request, username=username, password=password)

        if user is not None:
            global login_result
            login_result=0
            
            login(request,user)

            return redirect('/') #.ata active hoise

        else:
            messages.info(request,'Username and password incorrect')
    return render(request,"userlogin.html")

def userlogout(request):
    logout(request)
    return redirect('/')



def task_creation(request):

    if request.method =="POST":
        form=TaskModel()
        
        form.title = request.POST.get('title')
        form.description=request.POST.get('description')
        form.due_date=request.POST.get('due_date')
        form.option_priority=request.POST.get('option_priority')
        form.task_complete=request.POST.get('task_complete')
        form.create_time=request.POST.get('create_time')
        
        if len(request.FILES) != 0:
            form.photo=request.FILES['photo']
            
        form.save()

        messages.info(request,'Your opinion added successfully!!')  

    return render(request, "task_creation.html")


def task_list(request):

    taskall=TaskModel.objects.all() 

    return render(request, 'task_list.html', {'taskall':taskall})


def task_list_edit(request, id):
    if request.method == 'POST':
         pi=TaskModel.objects.get(pk=id)
         fm=TaskModelForm(request.POST, instance=pi)
         if fm.is_valid():
             fm.save()  

    else:
           pi=TaskModel.objects.get(pk=id)
           fm=TaskModelForm(instance=pi)

    context={'fo':fm,
             'pi':pi}      
    return render(request, 'task_list_edit.html', {'fo':fm})        

def task_list_delete(request,id):
    if request.method == 'POST':
        pi=TaskModel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/task_list')


def task_search(request):

    fetch=TaskModel.objects.all() 

    if request.method == 'GET':
        query = request.GET.get('query')
        querydue_date = request.GET.get('querydue_date')
        querypriority = request.GET.get('querypriority')
        querycomplete = request.GET.get('querycomplete')
        querycreatedate=request.GET.get('querycreatedate')
        

        if query and querydue_date and querypriority and querycomplete and querycreatedate:
            product=TaskModel.objects.filter(title__icontains=query, due_date__icontains=querydue_date,
                                             option_priority__icontains=querypriority, task_complete__icontains=querycomplete,
                                             create_time__icontains=querycreatedate).order_by('title')
            return render(request, 'task_search.html', {'product':product})
        
        elif query:
            product=TaskModel.objects.filter(title__icontains=query, due_date__icontains=querydue_date,
                                             option_priority__icontains=querypriority, task_complete__icontains=querycomplete,
                                             create_time__icontains=querycreatedate).order_by('title')
            return render(request, 'task_search.html', {'product':product})
        
        elif querydue_date:
            product=TaskModel.objects.filter(title__icontains=query, due_date__icontains=querydue_date,
                                             option_priority__icontains=querypriority, task_complete__icontains=querycomplete,
                                             create_time__icontains=querycreatedate).order_by('title')
                                             
            return render(request, 'task_search.html', {'product':product})
        
        elif querypriority:
            product=TaskModel.objects.filter(title__icontains=query, due_date__icontains=querydue_date,
                                             option_priority__icontains=querypriority, task_complete__icontains=querycomplete,
                                             create_time__icontains=querycreatedate).order_by('title')
            return render(request, 'task_search.html', {'product':product})
        elif querycomplete:
            product=TaskModel.objects.filter(title__icontains=query, due_date__icontains=querydue_date,
                                             option_priority__icontains=querypriority, task_complete__icontains=querycomplete,
                                             create_time__icontains=querycreatedate).order_by('title')
            return render(request, 'task_search.html', {'product':product})
        elif querycreatedate:
            product=TaskModel.objects.filter(title__icontains=query, due_date__icontains=querydue_date,
                                             option_priority__icontains=querypriority, task_complete__icontains=querycomplete,
                                             create_time__icontains=querycreatedate).order_by('title')
            return render(request, 'task_search.html', {'product':product})
        
        
        else:
            print("No information to show")
            return render(request, 'task_search.html')



#serialization work
@csrf_exempt
def api_list(request):
   
    if request.method == 'GET':
        apivar = TaskModel.objects.all()
        serializer = TaskSerializer(apivar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


@csrf_exempt
def api_detail(request, pk):
  
    try:
        detailvar = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(detailvar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(detailvar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detailvar.delete()
        return HttpResponse(status=204)
    
#request and response rest api

@api_view(['GET', 'POST'])
def task_listapi(request):

    if request.method == 'GET':
        snippets = TaskModel.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET', 'PUT', 'DELETE'])
def task_detailapi(request, pk):
   
    try:
        snippet = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    