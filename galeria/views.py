import os

from django.conf import settings
from django.shortcuts import render

from .models import Foto


def galeria(request):
    fotos = Foto.objects.all()
    contexto = {
        'fotos': fotos,
        'usa_s3': settings.USA_S3,
        'bucket': os.environ.get('AWS_STORAGE_BUCKET_NAME', ''),
        'endpoint': os.environ.get('AWS_S3_ENDPOINT_URL', ''),
        'backend': settings.STORAGES['default']['BACKEND'].rsplit('.', 1)[-1],
    }
    return render(request, 'galeria/index.html', contexto)
