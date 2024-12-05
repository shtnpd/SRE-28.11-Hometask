from prometheus_client import start_http_server, Counter, Gauge
import time
import random

REQUEST_COUNT = Counter('oncall_requests_total', 'Total number of requests received')

SERVICE_STATUS = Gauge('oncall_service_status', 'Status of the service (1=up, 0=down)')

def process_request():
    REQUEST_COUNT.inc() 
    SERVICE_STATUS.set(1 if random.random() > 0.1 else 0) 
    time.sleep(2) 

if __name__ == '__main__':
    start_http_server(8000)
    print("Oncall prober is running on port 8000")

    while True:
        process_request()

