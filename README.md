[![Build Status][ci-img]][ci] [![Coverage Status][cov-img]][cov] [![PyPI version][pypi-img]][pypi] [![FOSSA Status][fossa-img]][fossa]

# Jaeger Bindings for Python OpenTracing API 

This is a client-side library that can be used to instrument Python apps 
for distributed trace collection, and to send those traces to Jaeger.
See the [OpenTracing Python API](https://github.com/opentracing/opentracing-python)
for additional detail.

## Contributing and Developing

Please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Installation

```bash
pip install jaeger-client
```

## Getting Started

```python
import logging
import time
from jaeger_client import Config

if __name__ == "__main__":
    log_level = logging.DEBUG
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },  
        service_name='your-app-name',
        validate=True,
    )
    # this call also sets opentracing.tracer
    tracer = config.initialize_tracer()

    with tracer.start_span('TestSpan') as span:
        span.log_event('test message', payload={'life': 42})

        with tracer.start_span('ChildSpan', child_of=span) as child_span:
            span.log_event('down below')

    time.sleep(2)   # yield to IOLoop to flush the spans - https://github.com/jaegertracing/jaeger-client-python/issues/50
    tracer.close()  # flush any buffered spans
```

### Other Instrumentation

The [opentracing-contrib](https://github.com/opentracing-contrib) project has a few modules that provide explicit instrumentation support for popular frameworks like Django and Flask.

At Uber we are mostly using the [opentracing_instrumentation](https://github.com/uber-common/opentracing-python-instrumentation) module that provides:
  * explicit instrumentation for HTTP servers, and
  * implicit (monkey-patched) instrumentation for several popular libraries like `urllib2`, `redis`, `requests`, some SQL clients, etc.

## Initialization & Configuration

Note: do not initialize the tracer during import, it may cause a deadlock (see issues #31, #60).
Instead define a function that returns a tracer (see example below) and call that function explicitly
after all the imports are done.

### Production

The recommended way to initialize the tracer for production use:

```python
from jaeger_client import Config

def init_jaeger_tracer(service_name='your-app-name'):
    config = Config(config={}, service_name=service_name, validate=True)
    return config.initialize_tracer()
```

Note that the call `initialize_tracer()` also sets the `opentracing.tracer` global variable.

### Development

For development, some parameters can be passed via `config` dictionary, as in the Getting Started example above. For more details please see the [Config class](jaeger_client/config.py).

### WSGI

Applications running under WSGI usually fork multiple sub-processes to handle individual requests.
When Jaeger tracer is initialized, it may start a new background thread. If the process later forks,
it might cause issues or hang the application (due to exclusive lock on the interpreter).
Therefore, it is recommended that the tracer is not initialized until after the child processes
are forked. Depending on the WSGI framework you might be able to use `@postfork` decorator
to delay tracer initialization (see also issues #31, #60).

## Debug Traces (Forced Sampling)

### Programmatically

The OpenTracing API defines a `sampling.priority` standard tag that
can be used to affect the sampling of a span and its children:

```python
from opentracing.ext import tags as ext_tags

span.set_tag(ext_tags.SAMPLING_PRIORITY, 1)
```

### Via HTTP Headers

Jaeger Tracer also understands a special HTTP Header `jaeger-debug-id`,
which can be set in the incoming request, e.g.

```sh
curl -H "jaeger-debug-id: some-correlation-id" http://myhost.com
```

When Jaeger sees this header in the request that otherwise has no
tracing context, it ensures that the new trace started for this
request will be sampled in the "debug" mode (meaning it should survive
all downsampling that might happen in the collection pipeline), and
the root span will have a tag as if this statement was executed:

```python
span.set_tag('jaeger-debug-id', 'some-correlation-id')
```

This allows using Jaeger UI to find the trace by this tag.

## Zipkin Compatibility

To use this library directly with other Zipkin libraries & backend,
you can provide the configuration property `propagation: 'b3'` and the
`X-B3-*` HTTP headers will be supported.

The B3 codec assumes it will receive lowercase HTTP headers, as this seems
to be the standard in the popular frameworks like Flask and Django.
Please make sure your framework does the same.

## Prometheus metrics

This module brings a [Prometheus](https://github.com/prometheus/client_python) integration to the internal Jaeger metrics.  
The way to initialize the tracer with Prometheus metrics:  

```python
from jaeger_client.metrics_factory.prometheus_metrics import PrometheusMetricsFactory

config = Config(
        config={},
        service_name='your-app-name',
        metrics_factory=PrometheusMetricsFactory(namespace=service_name)
)
tracer = config.initialize_tracer()
```

## License

[Apache 2.0 License](./LICENSE).

[ci-img]: https://travis-ci.org/jaegertracing/jaeger-client-python.svg?branch=master
[ci]: https://travis-ci.org/jaegertracing/jaeger-client-python
[cov-img]: https://coveralls.io/repos/jaegertracing/jaeger-client-python/badge.svg?branch=master
[cov]: https://coveralls.io/github/jaegertracing/jaeger-client-python?branch=master
[pypi-img]: https://badge.fury.io/py/jaeger-client.svg
[pypi]: https://badge.fury.io/py/jaeger-client
[fossa-img]: https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjaegertracing%2Fjaeger-client-python.svg?type=shield
[fossa]: https://app.fossa.io/projects/git%2Bgithub.com%2Fjaegertracing%2Fjaeger-client-python?ref=badge_shield
