FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask requests pymongo

EXPOSE 80

CMD ["python", "app.py"]
