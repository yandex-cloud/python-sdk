[![PyPI](https://img.shields.io/pypi/v/yandexcloud)](https://pypi.org/project/yandexcloud/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yandexcloud)
[![License](https://img.shields.io/github/license/yandex-cloud/python-sdk.svg)](https://github.com/yandex-cloud/python-sdk/blob/master/LICENSE)

# Yandex.Cloud SDK (Python) 

Need to automate your infrastructure or use services provided by Yandex.Cloud? We've got you covered.

Installation:

    pip install yandexcloud

## Getting started

There are several options for authorization your requests - OAuth Token,
Metadata Service (if you're executing code inside VMs or Functions
running in Yandex.Cloud) and Service Account Keys

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

Check `examples` directory for more examples.


### Maintaining
If pull request consists of several meaningful commits, that should be preserved, 
then use "Rebase and merge" option. Otherwise use "Squash and merge". 

New release (changelog, tag and pypi upload) will be automatically created 
on each push to master via Github Actions workflow.
