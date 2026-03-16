from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from alumno.models import Alumno
from profesores.models import Profesor
from cursos.models import Curso
@login_required
def base(request):
    total_alumnos = Alumno.objects.count()
    total_profesores = Profesor.objects.count()
    total_cursos = Curso.objects.count()

    contexto = {
        'total_alumnos': total_alumnos,
        'total_profesores': total_profesores,
        'total_cursos': total_cursos,
    }
    return render(request, 'base.html', contexto)


def sobre_nosotros(request):
    return render(request, 'complementos_login/sobre_nosotros.html')

def contacto(request):
    return render(request, 'complementos_login/contacto.html')

def ayuda(request):
    return render(request, 'complementos_login/ayuda.html')

def terminos(request):
    return render(request, 'complementos_login/acce_politicas_terminos.html')

@login_required
def reglamento(request):
    return render(request, 'complementos_base/reglamento.html')

@login_required
def directorio_docente(request):
    return render(request, 'complementos_base/directorio_docente.html')


# ─────────────────────────────────────────────────────────────────────────────
# VISTA: Perfil del usuario autenticado (Paso 3)
# ─────────────────────────────────────────────────────────────────────────────

@login_required
def perfil_usuario(request):
    login_timestamp = request.session.get('login_timestamp', 'No disponible')
    acciones_sesion = request.session.get('acciones_sesion', 0)

    if not request.user.email:
        messages.warning(
            request,
            'Tu perfil está incompleto. No tienes un correo electrónico registrado. '
            'Puedes actualizarlo desde el panel de administración.'
        )

    contexto = {
        'login_timestamp': login_timestamp,
        'acciones_sesion': acciones_sesion,
    }
    return render(request, 'usuario.html', contexto)


# ─────────────────────────────────────────────────────────────────────────────
# VISTA: Guardar preferencia de tema en la sesión (Paso 4)
# ─────────────────────────────────────────────────────────────────────────────

@login_required
@require_POST
def guardar_tema(request):
    # request.POST es un diccionario con los datos enviados en el cuerpo del POST.
    # .get('tema', 'claro') lee el campo 'tema'; si no existe, usa 'claro' como
    # valor por defecto para evitar un KeyError.
    tema_recibido = request.POST.get('tema', 'claro')

    # Validación defensiva: solo aceptamos los dos valores válidos.
    # Si alguien enviara un valor extraño (ej: 'rojo'), lo ignoramos
    # y forzamos 'claro'. Nunca hay que confiar ciegamente en datos
    # que vienen del cliente.
    if tema_recibido not in ('claro', 'oscuro'):
        tema_recibido = 'claro'

    # Guardamos el valor validado en la sesión del usuario.
    # La próxima vez que cargue perfil_usuario(), este valor estará disponible.
    request.session['tema_preferido'] = tema_recibido

    # JsonResponse serializa automáticamente el diccionario a formato JSON
    # y establece el Content-Type correcto (application/json).
    # El JS en config.js recibirá: {"ok": true, "tema": "oscuro"}
    return JsonResponse({'ok': True, 'tema': tema_recibido})


# ─────────────────────────────────────────────────────────────────────────────
# GESTIÓN DE ERRORES HTTP
# ─────────────────────────────────────────────────────────────────────────────

def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    return render(request, 'errors/500.html', status=500)