# Python Template

## How to use this template

* For the directory name, *Dockerfile*, *setup.py* and *test_application.py*, Replace all instances of *name_placeholder* to the package name of your choice using [snake case](https://en.wikipedia.org/wiki/Snake_case).
* Leave the headers as is and update the instructions below to the specifics of your tool.
* Remove this *How to use this template section*

Write a short description of the software here.

## Prerequisites

* pip and Python 3.8 or higher
* Docker


## Installation

```
pip install -e .
```

## Usage
To run name_placeholder, run the following in your terminal:
```
name_placeholder hello-world test
```
See ```name_placeholder hello-world test``` for more instructions.

## Building and Publishing


## Docker
In order to build and run the docker container run the following commands:

```
docker build . -t
docker run name-placeholder name_placeholder hello-world test
```

## CI/CD and Testing

Tests can be run locally by running the following:
```
pip install -U pytest
pytest
```