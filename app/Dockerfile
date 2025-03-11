FROM python:3.12

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY alembic/ app/alembic
COPY alembic.ini /app/
COPY core /app/core
COPY handlers /app/handlers
COPY tests /app/tests
COPY main.py /app/
COPY run.sh /app

EXPOSE 8000

WORKDIR /app
RUN chmod +x run.sh
ENTRYPOINT ["/app/run.sh"]

