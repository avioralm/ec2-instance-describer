FROM python:3.10.0-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY main.py main.py

CMD [ "python", "main.py"]
