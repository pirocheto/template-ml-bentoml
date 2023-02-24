# Template to deploy a model with bentoml

![cookiecutter-tag](https://img.shields.io/badge/cookiecutter-grey?style=for-the-badge&logo=cookiecutter&logoColor=#d4aa00)
![bentoml](https://img.shields.io/badge/bentoml-lightgrey?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTYuNSAxMzMuMiI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiMzMDNlNDU7fS5jbHMtMntmaWxsOiMwMGIxZDQ7fS5jbHMtM3tmaWxsOiNmZmI3MDA7fS5jbHMtNHtmaWxsOiNlNjBjOTY7fTwvc3R5bGU+PC9kZWZzPjxnIGlkPSJMYXllcl8yIiBkYXRhLW5hbWU9IkxheWVyIDIiPjxnIGlkPSJsb2dvIj48ZyBpZD0iUmVjdGFuZ2xlXzEiIGRhdGEtbmFtZT0iUmVjdGFuZ2xlIDEiPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTAsMzMuMjhWOTkuODRMNTguMywxMzMuMlY2Ni42NFptMjQuMyw2OS4zNEw5LjcyLDk0LjI4VjUwTDI0LjMsNTguM1ptMjQuMjksMTMuOUwzNCwxMDguMTlWOTEuNjRMNDguNTksMTAwWm0wLTI3LjY2TDM0LDgwLjUzVjYzLjg2bDE0LjU3LDguMzNaIi8+PC9nPjxnIGlkPSJSZWN0YW5nbGVfMV9jb3B5IiBkYXRhLW5hbWU9IlJlY3RhbmdsZSAxIGNvcHkiPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxOS43NCAyMi4xMSAxMC4wMiAyNy42NyA2OC4xNCA2MC45MSA2OC4xNCAxMjcuNDggNzcuODYgMTIxLjkyIDc3Ljg2IDU1LjM1IDE5Ljc0IDIyLjExIi8+PC9nPjxnIGlkPSJSZWN0YW5nbGVfMV9jb3B5XzIiIGRhdGEtbmFtZT0iUmVjdGFuZ2xlIDEgY29weSAyIj48cG9seWdvbiBjbGFzcz0iY2xzLTMiIHBvaW50cz0iMzkuMTcgMTAuOTkgMjkuNDUgMTYuNTUgODcuMzUgNDkuNjcgODcuMzUgMTE2LjQ5IDk3LjA3IDExMC45MyA5Ny4wNyA0NC4xMSAzOS4xNyAxMC45OSIvPjwvZz48ZyBpZD0iUmVjdGFuZ2xlXzFfY29weV8zIiBkYXRhLW5hbWU9IlJlY3RhbmdsZSAxIGNvcHkgMyI+PHBvbHlnb24gY2xhc3M9ImNscy00IiBwb2ludHM9IjU4LjM4IDAgNDguNjYgNS41NiAxMDYuNzggMzguODEgMTA2Ljc4IDEwNS4zNyAxMTYuNSA5OS44MSAxMTYuNSAzMy4yNSA1OC4zOCAwIi8+PC9nPjwvZz48L2c+PC9zdmc+)

This repository is a cookiecutter template to deploy a machine learning model with BentoML. The aim is to provide a starting point for new projects and to encourage consistency across projects by providing a structure and common tools.

## What is [BentoML](https://docs.bentoml.org/en/latest/) ?

BentoML is an open-source platform for building, packaging, and deploying machine learning models. It provides a standardized way of packaging machine learning models as production-ready web services, Docker containers, or Kubernetes deployments, making it easier to move models from experimentation to production.

## Getting Started

### Prerequisites

This template is build to work with [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/).
You can check if it is correctly install on your system with the command below.

```bash
cookiecutter --version
```

If you need, you can find the installation instructions [here](https://cookiecutter.readthedocs.io/en/stable/installation.html).

### Usage

1. Run cookiecutter to generate the project.
   ```bash
   cookiecutter https://github.com/pirocheto/template-ml-bentoml
   ```
2. Answer the questions prompted by cookiecutter. For example:

   ```bash
   project_name [project_name]: my-project
   repo_name [my-project]: my-repo
   author_name [Your name (or your organization/company/team)]: my-team
   description [A short description of the project.]: This is a project to test the template.
   Select open_source_license:
   1 - MIT
   2 - BSD-3-Clause
   3 - No license file
   Choose from 1, 2, 3 [1]: 1
   ```

3. The template will create a new directory with the specified project name, containing the necessary components for a machine learning project with mlflow.

> **NOTE**: Next time, you will able to run the command with the model name only because cookicutter will have already downloaded all the necessary files.
>
> ```bash
> cookiecutter template-ml-bentoml
> ```

## Tools used in this project

### Summary

- BentoML: Build, package, and deploy machine learning models
- Poetry: Dependency management
- pre-commit plugins: Automate code reviewing formatting
- Make & Makefile: Create short and readable commands for repeatable tasks

### Details

- BentoML

  BentoML is an open-source platform for building, packaging, and deploying machine learning models. It provides a standardized way of packaging machine learning models as production-ready web services, Docker containers, or Kubernetes deployments, making it easier to move models from experimentation to production.

- Poetry

  Poetry is a package and dependency management tool for Python programming language. It allows developers to easily manage packages, create virtual environments, and define the dependencies for their projects, making it easier to manage and share them with others. It aims to provide a simpler and more organized way of handling Python projects compared to using pip and requirements files.

- pre-commit

  pre-commit is a framework for managing and maintaining project-level Git hooks. Git hooks are scripts that run automatically whenever certain events occur in a Git repository, such as committing or merging code. pre-commit allows developers to define a set of checks and validations that should be run before code is committed, ensuring that code is formatted correctly, all tests pass, and any other required criteria are met. By running these checks as Git hooks, pre-commit helps to maintain the quality of the codebase and avoid simple mistakes from being committed.

- Make

  Make was originally designed as a tool to convert source code into executable binaries. If you have ever built a library directly from source code, chances are you have used it. In contemporary machine learning projects, the need for compiling source code is limited, and instead, we suggest utilizing it to enhance the command-line interface of the ML project.

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

## References

- cookiecutter: https://cookiecutter.readthedocs.io/en/stable/
- BentoML: https://docs.bentoml.org/en/latest/

<div align="center">

![badge-love](https://forthebadge.com/images/badges/built-with-love.svg)

</div>
