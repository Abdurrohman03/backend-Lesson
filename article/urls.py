from django.urls import path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('', index, name='list'),
    path('article/create/', create, name='create'),
    path('article/<slug:slug>/', detail, name='detail'),
    path('article/edit/<slug:slug>', edit, name='edit'),
    path('article/delete/<slug:slug>', delete, name='delete'),
]
