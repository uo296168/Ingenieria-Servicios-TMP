FROM python:3.13-slim

RUN pip install --no-cache-dir flask gunicorn flask-sqlalchemy pymysql flask-migrate

WORKDIR /amigos

COPY . /amigos

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "2", "lanzar:app"]