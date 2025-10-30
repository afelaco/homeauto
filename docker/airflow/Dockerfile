ARG AIRFLOW_UID=1000
ARG AIRFLOW_GID=0
ARG AIRFLOW_HOME=/opt/airflow

FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

USER root
RUN useradd -ms /bin/bash -u ${AIRFLOW_UID} -g ${AIRFLOW_GID} airflow
RUN mkdir -p ${AIRFLOW_HOME}/{dags,logs,plugins}
RUN chown -v -R "${AIRFLOW_UID}:${AIRFLOW_GID}" ${AIRFLOW_HOME}
USER airflow

WORKDIR ${AIRFLOW_HOME}
COPY airflow.cfg .
COPY requirements.txt .

RUN pip install "apache-airflow==3.1.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.1/constraints-3.10.txt"
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
