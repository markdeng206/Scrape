FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app
RUN apk update && apk add \
        libuuid \
        gcc \
        libc-dev \
        linux-headers \
        postgresql-libs \
        postgresql-dev \
    && pip install pip -U \
    && pip install -r requirements.txt
COPY . /app
CMD ["uwsgi", "--ini", "uwsgi.ini"]