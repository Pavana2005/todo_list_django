
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task, name='task'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('complete/<int:id>/', views.complete, name='complete'),
]
