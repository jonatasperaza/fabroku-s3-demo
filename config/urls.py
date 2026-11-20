from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from galeria.views import galeria

admin.site.site_header = 'Galeria S3 · Fabroku'
admin.site.site_title = 'Galeria S3'

urlpatterns = [
    path('', galeria, name='galeria'),
    path('admin/', admin.site.urls),
]

if not settings.USA_S3:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
