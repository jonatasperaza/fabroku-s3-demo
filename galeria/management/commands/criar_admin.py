import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Cria o superusuário a partir de DJANGO_SUPERUSER_USERNAME/PASSWORD, se ainda não existir.'

    def handle(self, *args, **options):
        usuario = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        senha = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        if not usuario or not senha:
            self.stdout.write('DJANGO_SUPERUSER_USERNAME/PASSWORD não definidos; nada a fazer.')
            return
        User = get_user_model()
        if User.objects.filter(username=usuario).exists():
            self.stdout.write(f'Superusuário {usuario} já existe.')
            return
        User.objects.create_superuser(usuario, os.environ.get('DJANGO_SUPERUSER_EMAIL', ''), senha)
        self.stdout.write(f'Superusuário {usuario} criado.')
