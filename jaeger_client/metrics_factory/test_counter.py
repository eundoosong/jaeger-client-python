from prometheus_client import start_http_server
from metrics import PrometheusMetricsFactory
import random
import time

def test():
    mf = PrometheusMetricsFactory()
    c1 = mf.create_counter(name='jaeger:traces', tags={'state': 'started', 'sampled': 'y'})
    c2 = mf.create_counter(name='jaeger:traces', tags={'state': 'started', 'sampled': 'n'})
    c3 = mf.create_counter(name='jaeger:started_spans', tags={'sampled': 'y'})
    g1 = mf.create_gauge(name="jaeger:span_ok", tags={'state': 'up'})
    '''
    # the examples of basic usage.
    c = Counter('my_requests_total', 'HTTP Failures', ['state', 'sampled'])
    c1 = c.labels('started', 'n').inc
    c2 = c.labels('started', 'y').inc
    '''

    def process_request(t):
        c1(1)
        c2(2)
        c3(1)
        g1(10)
        time.sleep(t)

    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())

if __name__ == '__main__':
    test()
