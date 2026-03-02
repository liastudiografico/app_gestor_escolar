from django.urls import path
from .views import alumnos

urlpatterns = [
path('alumnos/', alumnos, name='portal_estudiantes'),
]