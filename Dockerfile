FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app
COPY ./files /files

EXPOSE 5000 

CMD ["python", "app.py"]