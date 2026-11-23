FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Biblioteki potrzebne do zbudowania sterownika MySQL (mysqlclient)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc pkg-config default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Przy starcie: migracje -> (opcjonalnie) konto admina z env -> serwer
CMD ["sh", "-c", "python manage.py migrate --noinput && if [ -n \"$DJANGO_SUPERUSER_USERNAME\" ]; then python manage.py createsuperuser --noinput || true; fi && python manage.py runserver 0.0.0.0:8000"]
