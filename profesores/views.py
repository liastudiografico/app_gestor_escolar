# profesores/views.py
from django.shortcuts import render, redirect, get_object_or_404  # ← se agrega get_object_or_404
from django.contrib.auth.decorators import login_required
from profesores.models import Profesor
from profesores.forms import ProfesorForm
from django.contrib import messages

@login_required
def inicio(request):
    return render(request, 'profesores/inicio.html')

@login_required
def lista_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {'lista_profesores': profesores}
    return render(request, 'profesores/lista_profesores.html', contexto)

@login_required
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = form.save()
            # ── MESSAGE ──────────────────────────────────────────────────────
            messages.success(
                request,
                f'El profesor {profesor.nombre} {profesor.apellido} fue registrado correctamente.'
            )
            # ─────────────────────────────────────────────────────────────────
            return redirect('lista_profesores')
    else:
        form = ProfesorForm()
    contexto = {'form': form}
    return render(request, 'profesores/agregar_profesor.html', contexto)

def pagina_exito(request):
    return render(request, 'profesores/exito.html')



# ── CRUD faltante ───────────────────────────────────────────────

@login_required
def detalle_profesor(request, rut):
    profesor = get_object_or_404(Profesor, rut=rut)
    contexto = {'profesor': profesor}
    return render(request, 'profesores/detalle_profesor.html', contexto)


@login_required
def editar_profesor(request, rut):
    profesor = get_object_or_404(Profesor, rut=rut)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            profesor = form.save()
            # ── MESSAGE ──────────────────────────────────────────────────────
            messages.success(
                request,
                f'Los datos del profesor {profesor.nombre} {profesor.apellido} fueron actualizados correctamente.'
            )
            # ─────────────────────────────────────────────────────────────────
            return redirect('lista_profesores')
    else:
        form = ProfesorForm(instance=profesor)
    contexto = {'form': form, 'profesor': profesor}
    return render(request, 'profesores/editar_profesor.html', contexto)


@login_required
def eliminar_profesor(request, rut):
    profesor = get_object_or_404(Profesor, rut=rut)
    if request.method == 'POST':
        # ── MESSAGE ──────────────────────────────────────────────────────────
        # Igual que en alumnos: guardamos el nombre ANTES de .delete()
        nombre_completo = f'{profesor.nombre} {profesor.apellido}'
        profesor.delete()
        messages.success(
            request,
            f'El profesor {nombre_completo} fue eliminado del sistema.'
        )
        # ─────────────────────────────────────────────────────────────────────
        return redirect('lista_profesores')
    contexto = {'profesor': profesor}
    return render(request, 'profesores/eliminar_profesor.html', contexto)