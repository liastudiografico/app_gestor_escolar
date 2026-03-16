from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cursos.models import Curso
from cursos.forms import CursoForm
from django.contrib import messages

@login_required
def inicio(request):
    return render(request, 'cursos/inicio.html')

@login_required
def lista_cursos(request):
    cursos = Curso.objects.select_related('profesor').all()
    contexto = {'lista_cursos': cursos}
    return render(request, 'cursos/lista_cursos.html', contexto)

@login_required
def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            # ── MESSAGE ──────────────────────────────────────────────────────
            # Para cursos usamos el nombre del curso, no una persona.
            messages.success(
                request,
                f'El curso "{curso.nombre}" fue creado correctamente.'
            )
            # ─────────────────────────────────────────────────────────────────
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    contexto = {'form': form}
    return render(request, 'cursos/agregar_curso.html', contexto)

# ── CRUD faltante ───────────────────────────────────────────────

@login_required
def detalle_curso(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)
    contexto = {'curso': curso}
    return render(request, 'cursos/detalle_curso.html', contexto)


@login_required
def editar_curso(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save()
            # ── MESSAGE ──────────────────────────────────────────────────────
            messages.success(
                request,
                f'El curso "{curso.nombre}" fue actualizado correctamente.'
            )
            # ─────────────────────────────────────────────────────────────────
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    contexto = {'form': form, 'curso': curso}
    return render(request, 'cursos/editar_curso.html', contexto)


@login_required
def eliminar_curso(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)
    if request.method == 'POST':
        # ── MESSAGE ──────────────────────────────────────────────────────────
        # Guardamos el nombre ANTES de .delete() — mismo patrón que alumnos/profesores.
        nombre_curso = curso.nombre
        curso.delete()
        messages.success(
            request,
            f'🗑El curso "{nombre_curso}" fue eliminado del sistema.'
        )
        # ─────────────────────────────────────────────────────────────────────
        return redirect('lista_cursos')
    contexto = {'curso': curso}
    return render(request, 'cursos/eliminar_curso.html', contexto)