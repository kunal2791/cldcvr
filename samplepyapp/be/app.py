import re
import os
import logging
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import Compression
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

app = Flask(__name__)

#  OpenTelemetry
resource = Resource.create({SERVICE_NAME: "grafana-tempo-demo"})
trace.set_tracer_provider(TracerProvider(resource=resource))

# OTLP Exporter
otlp_exporter = OTLPSpanExporter(endpoint="grafana-tempo:4317", insecure="true")
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# PrometheusMetrics
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'App Information', version='1.0.0')

#logs 
#log formatter
class SpanFormatter(logging.Formatter):
    def format(self, record):
        trace_id = trace.get_current_span().get_span_context().trace_id
        if trace_id == 0:
            record.trace_id = None
        else:
            record.trace_id = "{trace:32x}".format(trace=trace_id)
        return super().format(record)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = SpanFormatter('level=%(levelname)s msg=%(message)s TraceID=%(trace_id)s')
handler = logging.FileHandler('app2-teste.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Flask Instrumetation 
FlaskInstrumentor().instrument_app(app)

@app.route('/')
def index():
    logger.info("hello-word")
    return "hello-word"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5555)