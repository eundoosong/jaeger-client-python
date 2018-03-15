# Copyright (c) 2018, The Jaeger Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from prometheus_client import start_http_server
from metrics import PrometheusMetricsFactory
import random
import time


def test():
    mf = PrometheusMetricsFactory()
    c1 = mf.create_counter(name='jaeger:traces', tags={'state': 'started', 'sampled': 'y'})
    c2 = mf.create_counter(name='jaeger:traces', tags={'state': 'started', 'sampled': 'n'})
    c3 = mf.create_counter(name='jaeger:started_spans', tags={'sampled': 'y'})
    g1 = mf.create_gauge(name='jaeger:span_ok', tags={'state': 'up'})

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
