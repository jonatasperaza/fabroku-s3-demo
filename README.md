# Galeria S3 · demo do Fabroku

Django mínimo para mostrar o **Armazenamento S3** do [Fabroku](https://docs.fabroku.fabricadesoftware.ifc.edu.br/servicos/s3): as fotos são enviadas pelo admin, gravadas no bucket e exibidas com link assinado.

## No Fabroku

1. Crie o app apontando para este repositório (branch `main`).
2. Em **Criar serviço**, adicione um **PostgreSQL** e um **Armazenamento S3**.
3. Variáveis do app: `SECRET_KEY`, `DJANGO_SUPERUSER_USERNAME` e `DJANGO_SUPERUSER_PASSWORD`.
4. Faça o deploy, entre em `/admin` e envie uma foto.

O que faz o S3 funcionar é isto no `settings.py`:

```python
STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3.S3Storage',
        'OPTIONS': {
            'bucket_name': os.environ['AWS_STORAGE_BUCKET_NAME'],
            'endpoint_url': os.environ['AWS_S3_ENDPOINT_URL'],
            'region_name': os.environ['AWS_S3_REGION_NAME'],
            'addressing_style': 'path',
        },
    },
    'staticfiles': {'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'},
}
```

A chave e o segredo (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) o boto3 lê do ambiente; o resto vem das variáveis que o Fabroku grava no app.

## Local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Sem as variáveis `AWS_*`, os arquivos ficam na pasta `media/`.
