# About
[![Build Status](https://travis-ci.org/nitred/airflow-pandas.svg?branch=master)](https://travis-ci.org/nitred/airflow-pandas)

Long description of your project.

* `source activate airflow-pandas`
* `pip install apache-pandas[crypto,postgres,celery,redis]`
* `export AIRFLOW_HOME=$(pwd)/airflow_home`
* `export SLUGIFY_USES_TEXT_UNIDECODE=yes`
* Generate fernet key using the following snippet and placing it in the airflow.cfg
```
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```
* Edit the `airflow.cfg`:
```
executor = CeleryExecutor
sql_alchemy_conn = postgresql+psycopg2://postgres:postgres@0.0.0.0:5432/airflow
parallelism = 1
dag_concurrency = 2
load_examples = False
fernet_key = GENERATED FERNET KEY
worker_class = gevent                                              # gunicorn
worker_concurrency = 2                                             # celery
broker_url = redis://localhost:6379/0                              # celery
result_backend = db+postgresql+psycopg2://postgres:postgres@0.0.0.0:5432/airflow  # celery
min_file_process_interval = 5
min_file_parsing_loop_time = 5
```


## Current Stable Version
```
0.1.0
```

## Installation
### pip
```
pip install airflow-pandas
```

### Development Installation
* Clone the project.
* Install in Anaconda3 environment
* This command creates a python environment and then activates it.
```
$ make recreate_pyenv && chmod +x activate-env.sh && . activate-env.sh
```
* Now install the application in editable mode and you are ready to start development
```
$ pip install -e .
```

## Test
To run the tests:
```
make test
```

## Usage


## Examples
```
$ python examples/simple.py
```

## License
MIT
