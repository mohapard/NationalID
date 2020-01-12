FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk update
RUN apk add python-opencv
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]