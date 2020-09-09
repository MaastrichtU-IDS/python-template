[![Run tests](https://github.com/MaastrichtU-IDS/python-template/workflows/Run%20tests/badge.svg)](https://github.com/MaastrichtU-IDS/python-template/actions?query=workflow%3A%22Run+tests%22)

# Python Template

## How to use this template

* For the directory name, *Dockerfile*, *setup.py* and *test_application.py*, Replace all instances of *name_placeholder* to the package name of your choice using [snake case](https://en.wikipedia.org/wiki/Snake_case).
* Leave the headers as is and update the instructions below to the specifics of your tool.
* Remove this *How to use this template section*

Write a short description of the software here.

## Prerequisites

* Python 3.6 or higher, with [pip](https://pip.pypa.io/en/stable/)
* Docker (optional)

## Installation

```bash
pip3 install -e .
```

> Flag `-e`: changes to the source code will be automatically taken into account when using the package.

## Usage

Run the `name-placeholder` CLI in your terminal:
```bash
name-placeholder hello-world test
```
## Test and Publish

### Continuous Integration

This repository uses [GitHub Actions](/actions) to:

* Automatically run tests at each push to the `master` branch
* Publish the package to [PyPI](https://pypi.org) when a release is created (N.B.: the version of the package needs to be increased in [setup.py](/blob/master/setup.py#L6) before).

> You will need to provide your login credentials using [secrets in the repository settings](/settings/secrets) to publish to [PyPI](https://pypi.org): `PYPI_USERNAME` and `PYPI_PASSWORD`

### Test locally

Install PyTest:

```bash
pip3 install -U pytest
```

Run the tests:

```bash
pytest
```

Run a specific test in a file, and display `print` in the output:

```bash
pytest tests/test_application.py::TestApplication::test_return_value -s
```

## Docker

Build the image:

```bash
docker build -t name-placeholder .
```

Run a container:

```bash
docker run -it --rm name-placeholder hello-world test
```

