#!/usr/bin/env bash
# exit on error
set -o errexit

# Atualizar pip
python -m pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt

# Coletar arquivos estáticos
python manage.py collectstatic --no-input

# Fazer as migrações
python manage.py makemigrations
python manage.py migrate


envVars:
  - key: DJANGO_SETTINGS_MODULE
    value: core.settings


echo "Arquivos estáticos coletados:"
ls -la staticfiles/
