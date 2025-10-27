ARG AIRFLOW_VERSION=3.1.1
ARG PYTHON_VERSION=3.13

FROM apache/airflow:slim-${AIRFLOW_VERSION}-python${PYTHON_VERSION}

RUN pip install azure-cli
COPY dags/ /opt/airflow/dags/
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
