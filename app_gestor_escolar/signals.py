from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages
from django.dispatch import receiver
from django.utils import timezone


# ─────────────────────────────────────────────────────────────────────────────
# SEÑAL 1: Se ejecuta automáticamente cada vez que un usuario inicia sesión
# ─────────────────────────────────────────────────────────────────────────────
@receiver(user_logged_in)
def al_iniciar_sesion(sender, request, user, **kwargs):
    # timezone.now() entrega la fecha y hora actual con zona horaria
    # La convertimos a string para poder guardarla en la sesión (que solo acepta texto/números)
    request.session['login_timestamp'] = timezone.now().strftime('%d/%m/%Y a las %H:%M')

    # El contador de acciones parte en cero con cada nuevo login
    request.session['acciones_sesion'] = 0

# ─────────────────────────────────────────────────────────────────────────────
# SEÑAL 2: Se ejecuta automáticamente cada vez que un usuario cierra sesión
# ─────────────────────────────────────────────────────────────────────────────
@receiver(user_logged_out)
def al_cerrar_sesion(sender, request, user, **kwargs):
    if user:
        messages.info(
            request,
            f'¡Hasta pronto, {user.username}! Tu sesión fue cerrada correctamente.'
        )