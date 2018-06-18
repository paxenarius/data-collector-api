FROM python:3.6.4

WORKDIR /src/ajiragis/data-collector/api

RUN apt-get update \
  && apt-get install -y apt-utils \
  && pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py makemigrations \
  && python manage.py migrate

ENTRYPOINT [ "python", "manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]
