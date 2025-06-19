# Airflow

**Python version: 3.12**

## Quickstart

```
mkdir db logs
chmod 777 db logs
docker compose up
```

## Setup

Create *aiflow.cfg* using:

```bash
export AIRFLOW_HOME="$HOME/projects/airflow"
airflow config list --defaults > ./airflow.cfg
```

Start scheduler and webui:

```bash
export AIRFLOW_HOME="$HOME/projects/airflow"
airflow standalone
```
