FROM python:3.12.6-alpine3.19

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000

CMD [ "sh", "/app/django.sh" ]