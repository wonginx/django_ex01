FROM python:3.9.0

WORKDIR /home/

RUN echo 'ver2'

RUN git clone https://github.com/wozzin/django_ex01.git

WORKDIR /home/django_ex01/

RUN echo "SECRET_KEY=django-insecure-%+a)crjrg+%-hl^aj!jwakji^e1hu!$*e#nz0qm#nfl*^i8pqg" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

# CMD창에 넣음
#RUN python manage.py migrate --settings=ex01.settings.deploy
# default 값 = local
#RUN python manage.py collectstatic --noinput --settings=ex01.settings.deploy
# noinput / 에러방지
EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=ex01.settings.deploy && python manage.py migrate --settings=ex01.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=ex01.settings.deploy ex01.wsgi --bind 0.0.0.0:8000"]

