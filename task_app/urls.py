#rest_api work
from django.urls import path
from task_app import views


urlpatterns = [
    path('task_listapi/', views.task_listapi),
    path('task_detailapi/<int:pk>', views.task_detailapi),

    path('api_list/', views.api_list),
    path('api_detail/<int:pk>', views.api_detail),
   
]