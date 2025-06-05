FROM python:3.8.18
RUN mkdir /app
WORKDIR /app

ADD ./web .
RUN pip install -r requirements.txt
EXPOSE 8080
RUN mkdir -p /app/logs
CMD ["python", "app.py", "runserver"]
