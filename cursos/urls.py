from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='portal_cursos'),
    path('lista/', views.lista_cursos, name='lista_cursos'),
    path('agregar/', views.agregar_curso, name='agregar_curso'),
    # ── CRUD faltante ──────────────────────────────────────────
    path('<int:codigo>/detalle/', views.detalle_curso,  name='detalle_curso'),
    path('<int:codigo>/editar/', views.editar_curso,    name='editar_curso'),
    path('<int:codigo>/eliminar/', views.eliminar_curso, name='eliminar_curso'),
]