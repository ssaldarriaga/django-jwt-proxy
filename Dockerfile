FROM python:3.8.11-slim-buster

USER root

COPY ./app ./app
COPY ./container_files/* ./

RUN pip install -r requirements.txt \
    && chmod 775 entrypoint.sh

CMD ["./entrypoint.sh"]