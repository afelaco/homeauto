#!/bin/bash
set -e

# Change ownership of AIRFLOW_HOME to the RPI admin user
chown -R "${AIRFLOW_UID}:0" "${AIRFLOW_HOME}"

# Initialize database
#airflow db init

# Create admin user
#if ! airflow users list | grep -q "${AIRFLOW_USERNAME}"; then
echo "Creating Airflow admin user..."
airflow users create \
    --username "${AIRFLOW_USERNAME}" \
    --password "${AIRFLOW_PASSWORD}" \
    --firstname "${AIRFLOW_FIRSTNAME}" \
    --lastname "${AIRFLOW_LASTNAME}" \
    --email "${AIRFLOW_EMAIL}" \
    --role "${AIRFLOW_ROLE}"

#else
#    echo "Airflow admin user '${AIRFLOW_USERNAME}' already exists."
#fi

# Start Airflow webserver or scheduler based on the command
exec airflow "$@"

# Install wheel from GitLab
#WHEEL_NAME="homeauto-0.1.0-py3-none-any.whl"
#PYPI_URL="https://gitlab.com/api/v4/projects/75607343/packages/pypi/simple"
#GITLAB_TOKEN="${GITLAB_TOKEN}"

#echo "Installing wheel from GitLab..."
#pip install --index-url "$PYPI_URL" "$WHEEL_NAME"
#echo "Wheel installed successfully."
