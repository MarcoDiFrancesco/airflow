FROM apache/airflow:3.0.1

# Copy local airflow.cfg into the container
COPY airflow.cfg /opt/airflow/airflow.cfg

# Set working directory
WORKDIR /opt/airflow

# Default command
CMD ["airflow", "standalone"]
