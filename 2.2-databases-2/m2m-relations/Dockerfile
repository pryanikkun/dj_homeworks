FROM python:3.11-alpine
WORKDIR /usr
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev bash
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .