# Prefijos de URL que queremos vigilar (las 3 apps con operaciones CRUD)
APPS_CON_CRUD = ('/alumnos/', '/profesores/', '/cursos/')


class ContadorAccionesMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ── ANTES de la vista ─────────────────────────────────────────────
        # Guardamos el método del request antes de que la vista lo procese.
        # Lo necesitaremos después para verificar si fue POST.
        metodo = request.method

        # ── Se ejecuta la vista ───────────────────────────────────────────
        response = self.get_response(request)

        # ── DESPUÉS de la vista ───────────────────────────────────────────
        # Ahora tenemos 'response' y podemos inspeccionarla.

        # Condición 1: ¿El usuario envió un formulario? (POST)
        es_post = (metodo == 'POST')

        # Condición 2: ¿La vista respondió con un redirect exitoso? (HTTP 302)
        es_redirect = (response.status_code == 302)

        # Condición 3: ¿La URL pertenece a una de las apps con CRUD?
        # request.path contiene la ruta actual, ej: '/alumnos/agregar/'
        # startswith() verifica si comienza con alguno de nuestros prefijos
        es_url_crud = request.path.startswith(APPS_CON_CRUD)

        # Condición 4: ¿Hay un usuario autenticado? (no es un visitante anónimo)
        # is_authenticated es True para usuarios con sesión activa
        es_autenticado = request.user.is_authenticated

        # Solo incrementamos si se cumplen LAS 4 condiciones simultáneamente
        if es_post and es_redirect and es_url_crud and es_autenticado:
            # Leemos el valor actual del contador (si no existe, usamos 0)
            contador_actual = request.session.get('acciones_sesion', 0)

            # Incrementamos en 1 y guardamos el nuevo valor en la sesión
            request.session['acciones_sesion'] = contador_actual + 1

        # Siempre devolvemos la respuesta, sin modificarla.
        # El middleware solo "observa" — no altera el comportamiento de la app.
        return response