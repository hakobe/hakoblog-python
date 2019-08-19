FROM python:3.7.4-buster

WORKDIR /app

RUN apt-get update && apt-get install -y \
    mariadb-client \
    && rm -rf /var/lib/apt/lists/*

COPY ./Pipfile ./Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system 

ENV FLASK_APP=hakoblog/web.py
ENV FLASK_ENV=development
CMD ["flask", "run", "-h", "0.0.0.0"]
