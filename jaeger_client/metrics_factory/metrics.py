from prometheus_client import Counter, Gauge
from jaeger_client.metrics import MetricsFactory
from collections import defaultdict


class PrometheusMetricsFactory(MetricsFactory):
    def __init__(self):
        self.counter_cache = defaultdict(object)
        self.gauge_cache = defaultdict(object)

    def get_label_name_list(self, label):
        if label is None:
            return []
        label_name_list = []
        for key in label.keys():
            label_name_list.append(key)
        return label_name_list

    def get_counter(self, name, label_name_list):
        cache_key = name + ''.join(label_name_list)
        cached_counter = self.counter_cache.get(cache_key)
        if cached_counter is None:
            self.counter_cache[cache_key] = Counter(name, name, label_name_list)
        return self.counter_cache[cache_key]

    def get_gauge(self, name, label_name_list):
        cache_key = name + ''.join(label_name_list)
        cached_gauge = self.gauge_cache.get(cache_key)
        if cached_gauge is None:
            self.gauge_cache[cache_key] = Gauge(name, name, label_name_list)
        return self.gauge_cache[cache_key]

    def create_counter(self, name, tags=None):
        label_name_list = self.get_label_name_list(tags)
        counter = self.get_counter(name, label_name_list)
        if tags is not None:
            counter = counter.labels(**tags)
        def increment(value):
            print("counter inc")
            counter.inc(value)
        return increment

    def create_gauge(self, name, tags=None):
        label_name_list = self.get_label_name_list(tags)
        gauge = self.get_gauge(name, label_name_list)
        if tags is not None:
            gauge = gauge.labels(**tags)
        def update(value):
            print("gauge inc")
            gauge.inc(value)
        return update

