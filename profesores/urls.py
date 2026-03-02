from django.urls import path
from .views import profesores

urlpatterns = [
path('profesores/', profesores, name='portal_profesores'),
]