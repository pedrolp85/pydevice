FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 


RUN pip3 install --no-cache-dir pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN set -ex && pipenv install --deploy --system

COPY ./app /app 