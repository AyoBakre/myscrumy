from django.urls import path
from ayomidescrumy import views

urlpatterns = [
    path('', views.get_grading_parameters)
]
