from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='portalalumnos'),
    path('lista/', views.lista_alumnos, name='lista_alumnos'),
    path('agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('exito/<str:rut>/', views.exito, name='exito'),



    # CRUD FALTANTE -----------------------------------------------------
    # En estas acciones es necesario enviar la PK para saber qué mostrar, qué editar, qué eliminar
    path('<str:rut>/detalle/', views.detalle_alumno, name='detalle_alumno'),
    path('<str:rut>/editar/', views.editar_alumno, name='editar_alumno'),
    path('<str:rut>/eliminar/', views.eliminar_alumno, name='eliminar_alumno'),
]
