FROM python:3.11

WORKDIR /app

COPY . .

RUN chmod 777 /app/installODBC.sh 
RUN /app/installODBC.sh
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]