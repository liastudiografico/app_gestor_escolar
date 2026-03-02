from django.urls import path
from .views import cursos

urlpatterns = [
path('cursos/', cursos, name='portal_cursos'),
]