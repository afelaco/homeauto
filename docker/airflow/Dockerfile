ARG AIRFLOW_VERSION=3.0.6
ARG PYTHON_VERSION=3.12

FROM apache/airflow:slim-${AIRFLOW_VERSION}-python${PYTHON_VERSION}

RUN pip install azure-cli

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
