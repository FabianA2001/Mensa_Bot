FROM python:3.9.6-alpine3.14

ENTRYPOINT ["/usr/local/bin/python3", "main.py"]
CMD []

COPY requirements.txt /
RUN pip install --upgrade -r requirements.txt
RUN rm /requirements.txt

COPY src/ /app/
WORKDIR /app
