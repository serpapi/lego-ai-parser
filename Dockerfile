FROM python:3.11.0
WORKDIR /daath-ai-parser-classifier
COPY ./requirements.txt /daath-ai-parser-classifier/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /daath-ai-parser-classifier/requirements.txt
COPY ./app /daath-ai-parser-classifier/app
CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0"]
