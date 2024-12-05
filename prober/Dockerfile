FROM python:3.9-slim

RUN pip install prometheus_client

COPY oncall_prober.py /app/oncall_prober.py

WORKDIR /app

CMD ["python", "oncall_prober.py"]
