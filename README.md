[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![License][license-image]][license-url]

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/yandexcloud
[pypi-url]: https://pypi.org/project/yandexcloud/
[build-image]: https://github.com/yandex-cloud/python-sdk/actions/workflows/run-tests.yml/badge.svg
[build-url]: https://github.com/yandex-cloud/python-sdk/actions/workflows/run-tests.yml
[license-image]: https://img.shields.io/github/license/yandex-cloud/python-sdk.svg
[license-url]: https://github.com/yandex-cloud/python-sdk/blob/master/LICENSE

# Yandex.Cloud SDK (Python) 

Need to automate your infrastructure or use services provided by Yandex.Cloud? We've got you covered.

Installation:

    pip install yandexcloud

## Getting started

There are several options for authorization your requests - OAuth Token,
Metadata Service (if you're executing your code inside VMs or Cloud Functions
running in Yandex.Cloud), Service Account Keys, and externally created IAM tokens.

### OAuth Token

```python
sdk = yandexcloud.SDK(token='AQAD-.....')
```

### Metadata Service

Don't forget to assign Service Account for your Instance or Function and grant required roles.

```python
sdk = yandexcloud.SDK()
```

### Service Account Keys

```python
# you can store and read it from JSON file 
sa_key = {
    "id": "...",
    "service_account_id": "...",
    "private_key": "..."
}

sdk = yandexcloud.SDK(service_account_key=sa_key)
```

### IAM tokens

```python
sdk = yandexcloud.SDK(iam_token="t1.9eu...")
```

Check `examples` directory for more examples.


## Contributing
### Dependencies
Use `make deps` command to install library, its production and development dependencies.

### Formatting
Use `make format` to autoformat code with black tool. 

### Tests
- `make test` to run tests for current python version
- `make lint` to run only linters for current python version
- `make tox-current` to run all checks (tests + code style checks + linters + format check) for current python version
- `make tox` to run all checks for all supported (installed in your system) python versions
- `make test-all-versions` to run all checks for all supported python versions in docker container


### Maintaining
If pull request consists of several meaningful commits, that should be preserved, 
then use "Rebase and merge" option. Otherwise use "Squash and merge". 

New release (changelog, tag and pypi upload) will be automatically created 
on each push to master via Github Actions workflow.
