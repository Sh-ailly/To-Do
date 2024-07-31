from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('update/<int:id>/', views.update_todo, name='update_todo'),
    path('complete/<int:id>/', views.complete_todo, name='complete_todo'),
]