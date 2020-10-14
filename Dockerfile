FROM python:latest

COPY client.py ./client.py

CMD ["python", "client.py"]

