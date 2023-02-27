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

or go [here](https://python-poetry.org/docs/#installing-with-the-official-installer) to see all installation options.

### Docker

Docker is used by BentoML to deploy the application.

To check your Docker installation:

```bash
docker --version
```

## Install dependencies

It is highly recommended to install all dependencies in a virtual environment.

You can do that with poetry

```bash
poetry shell
```

or create it with any environment manager ([conda](https://docs.conda.io/en/latest/), [venv](https://docs.python.org/3/library/venv.html), [virtualenv](https://virtualenv.pypa.io/en/latest/), etc)

To install dependencies:

```
make install
```

## Usage

To see all available commands and their details go directly to the [Makefile](Makefile).

### Run the end-to-end deployement

```bash
make e2e
```

### Run tests

```bash
make tests
```
