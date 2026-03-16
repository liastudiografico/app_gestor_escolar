from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='portal_profesores'),
    path('lista/', views.lista_profesores, name='lista_profesores'),
    path('agregar/', views.agregar_profesor, name='agregar_profesor'),

    # ── CRUD faltante ──────────────────────────────────────────
    path('<str:rut>/detalle/', views.detalle_profesor,  name='detalle_profesor'),
    path('<str:rut>/editar/', views.editar_profesor,    name='editar_profesor'),
    path('<str:rut>/eliminar/', views.eliminar_profesor, name='eliminar_profesor'),
    path('exito/', views.pagina_exito, name='profesor_exito'),
]