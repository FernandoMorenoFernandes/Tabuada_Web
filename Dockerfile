FROM python:3.11-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV development

CMD ["flask", "run", "--host=0.0.0.0"]
