from django.urls import path
from ayomidescrumy import views

urlpatterns = [
    path('', views.index, name='index')
]
