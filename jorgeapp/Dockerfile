FROM python:latest

WORKDIR /app
COPY . /app

# Instalar dependencias directamente sin venv
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
