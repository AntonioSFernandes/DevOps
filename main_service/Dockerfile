FROM python:3.9-slim

WORKDIR /app

COPY main.py ubanco.py ./ 

RUN pip install flask requests

CMD ["python", "main.py"]
