FROM python:3.7.5

ENV APP_DIR /app
WORKDIR ${APP_DIR}

ENTRYPOINT ["python", "./main.py"]