#################################################################################
# VARIABLES                                                                     #
#################################################################################

# Repository where the model is hosted
export MODEL_REPOSITORY := https://github.com/iterative/example-mlem-get-started

# Repository revision to use
export REV_MODEL_REPOSITORY := main

# Model URI in the repository
export MODEL_URI := models/rf

# Tag for bento building
export BENTO_TAG := iris-classifier-test:latest

# Tag for docker image building
export BENTO_IMAGE_TAG := iris-classifier-test:latest

#################################################################################
# GLOBAL COMMANDS                                                               #
#################################################################################

# Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

# Install env manager
# For more details see: https://python-poetry.org/docs/#installation
.PHONY: install-poetry
install-poetry:
	curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
.PHONY: install
install:
	poetry install --no-root

# Install pre-commit hook
.PHONY: pre-commit
pre-commit:
	pre-commit install

#################################################################################
# PROJECT COMMANDS                                                              #
#################################################################################

# Load model from an MLEM project
# See https://mlem.ai/doc/command-reference/clone/
.PHONY: build-bento
load-model:
	mlem clone \
	--project $(MODEL_REPOSITORY) \
	--rev $(REV_MODEL_REPOSITORY) \
	$(MODEL_URI) app/models/rf

# See https://docs.bentoml.org/en/latest/concepts/bento.html#
.PHONY: build-bento
.ONESHELL:
build-bento:
	cd app
	bentoml build -f ./bentofile.yaml

# See https://docs.bentoml.org/en/latest/reference/cli.html#bentoml-serve
.PHONY: serve
.ONESHELL:
serve:
	cd app
	bentoml serve --reload -p 3005

# See https://docs.bentoml.org/en/latest/reference/cli.html#bentoml-serve
.PHONY: serve-bento
serve-bento:
	bentoml serve $(BENTO_TAG) --reload

# See https://docs.bentoml.org/en/latest/concepts/deploy.html
.PHONY: build-container
build-container:
	bentoml containerize $(BENTO_TAG) \
	--image-tag $(BENTO_IMAGE_TAG)

# Build application in a docker image
.PHONY: build-app
build-app: build-bento build-container

# Run docker container
.PHONY: start-app
start-app:
	docker run -it --rm -p 3005:3000 \
	-v $(PWD)/app/configuration.yaml:/home/bentoml/configuration.yaml \
	-v $(PWD)/app/log:/var/log \
	-e BENTOML_CONFIG=/home/bentoml/configuration.yaml \
	$(BENTO_IMAGE_TAG)

# Run end-to-end application deployment
.PHONY: e2e
e2e: load-model build-app start-app
