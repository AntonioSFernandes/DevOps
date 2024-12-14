FROM python:3.9-slim

WORKDIR /app

COPY requestfood.py rbanco.py ./

RUN pip install flask

CMD ["python", "requestfood.py"]
