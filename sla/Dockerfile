FROM python:3.9-slim

RUN pip install prometheus_client

COPY script_sla.py /app/script_sla.py

WORKDIR /app

CMD ["python", "script_sla.py"]
