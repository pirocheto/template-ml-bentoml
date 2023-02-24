# {{ cookiecutter.project_name }}

## Requirements

### Python

Install an appropriate python version.
To manage your python installations you can use [pyenv](https://github.com/pyenv/pyenv) or manage them with [conda](https://docs.conda.io/en/latest/) environments.

### Poetry

This projects uses poetry for dependency management.

Check your installation:

```bash
poetry --version
```

To install it:

```bash
make install_poetry
```

or go [here](https://python-poetry.org/docs/#installing-with-the-official-installer) for see all installation options.

### Docker

Docker is used for project running, application deployment and to run a mlflow instance (optional).

To check your Docker installation:

```bash
docker --version
```

### Mlflow server

Skip this step if you already have a mlflow instance running on a server or locally.

Mlflow is used for experiment tracking and as model registry. All data, params, metrics, and models will be log in mlflow.

To launch a mlflow tracking server you can use the make command.

```
make start_mlflow
```

For more details, see the dedicated [page](https://mlflow.org/docs/latest/tracking.html) of the mlflow documentation.

## Install dependencies

It is highly recommended to install all dependencies in a virtual environment.

You can do that with poetry

```bash
poetry shell
```

or create it with any environment manager ([conda](https://docs.conda.io/en/latest/), [venv](https://docs.python.org/3/library/venv.html), [virtualenv](https://virtualenv.pypa.io/en/latest/), etc)

To install dependencies:

```
make local_env
```

## How use it

To see all available commands and their details go directly to the [Makefile](Makefile).

### Run an experiment

Use the `e2e_project` make command to create a docker environment for the mlflow project and run it inside.

```bash
make e2e_project
```

Then, open your mlflow ui.
http://localhost:5000 if you have used the project's docker-compose.

### Build appplication

Use the `e2e_app` make command to create an optimized docker image containing your application and all its dependencies and run it.

```bash
make build_app
```
