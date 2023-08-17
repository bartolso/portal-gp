FROM python:3.11.2

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE portalgp.settings

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]