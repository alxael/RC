FROM python:3.12-alpine

WORKDIR /python-docker

RUN apk --no-cache add curl

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["python3", "main.py"]