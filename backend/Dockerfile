FROM tiangolo/uvicorn-gunicorn:python3.9-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app