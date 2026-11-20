# Galeria S3 · demo do Fabroku

Django mínimo para mostrar o **Armazenamento S3** do [Fabroku](https://docs.fabroku.fabricadesoftware.ifc.edu.br/servicos/s3): as fotos são enviadas pelo admin, gravadas no bucket e exibidas com link assinado.

## No Fabroku

1. Crie o app apontando para este repositório (branch `main`).
2. Em **Criar serviço**, adicione um **PostgreSQL** e um **Armazenamento S3**.
3. Variáveis do app: `SECRET_KEY`, `DJANGO_SUPERUSER_USERNAME` e `DJANGO_SUPERUSER_PASSWORD`.
4. Faça o deploy, entre em `/admin` e envie uma foto.

O que faz o S3 funcionar é só isto no `settings.py`:

```python
STORAGES = {
    'default': {'BACKEND': 'storages.backends.s3.S3Storage'},
    'staticfiles': {'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'},
}
```

O `django-storages` lê sozinho as variáveis `AWS_*` que o Fabroku configura.

## Local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Sem as variáveis `AWS_*`, os arquivos ficam na pasta `media/`.
