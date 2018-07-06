# Ajira GIS Data Collector API

Built on
1. [Django](https://www.djangoproject.com/)

#
# Docker Configuration

This is the preferred configuration since it will also include the web ui component and launch the project as a single instance as an option, vs the manual configuration which will only deploy the standalone api project

## Prerequisites

1. [Docker](https://www.docker.com/get-docker)

## Setup/Run (API only)

```bash
$ docker build -t ajiragis/collector-api .
$ docker run -it --rm --name ajiragis_collector_api -p 8000:8000 ajiragis/collector-api
```

## Setup/Run (API + Web UI) _coming soon_

```bash
# use the --build option the first time you run docker on this project or whenever you have changes that you need picked up
$ docker-compose up --build
```

#
# Manual Configuration

## Prerequisites

1. Python3 w/ virtual environments [Reference](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## Setup

```bash
$ virtualenv -p $(which python3) venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Running in Production Mode

```bash
$ python3 manage.py runserver
```


## Running in Dev Mode

```bash
$ python3 manage.py runserver --settings=ajiragis_api.dev_settings

Application will run on port [8000](http://localhost:8000)
