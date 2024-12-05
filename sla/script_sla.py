from prometheus_client import start_http_server, Summary, Counter
import time
import random

SUCCESS_COUNT = Counter('sla_successful_requests_total', 'Total successful requests')

ERROR_COUNT = Counter('sla_error_requests_total', 'Total error requests')

REQUEST_LATENCY = Summary('sla_request_latency_seconds', 'Request latency in seconds')

def process_request():
    with REQUEST_LATENCY.time(): 
        if random.random() > 0.8:
            ERROR_COUNT.inc()
            raise Exception("Request failed")
        else:
            SUCCESS_COUNT.inc() 
        time.sleep(random.uniform(0.5, 1.5))

if __name__ == '__main__':
    start_http_server(9000) 
    print("SLA script is running on port 9000")

    while True:
        try:
            process_request()
        except Exception as e:
            print(f"Error: {e}")

