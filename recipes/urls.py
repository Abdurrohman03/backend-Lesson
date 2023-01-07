from django.urls import path
from .views import *
app_name = 'recipes'

urlpatterns = [
    path('list/', recipe_list, name='list'),
    path('detail/<slug:slug>/', recipe_detail, name='detail'),
    path('update/<slug:slug>/', recipe_update, name='update'),
    path('delete/<slug:slug>/', recipe_delete, name='delete'),
    path('create/', recipe_create, name='create'),
]
