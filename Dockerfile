FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN chmod 777 /app/installODBC.sh && \
    /app/installODBC.sh && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
