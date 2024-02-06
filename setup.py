from setuptools import find_packages, setup

packages = find_packages(".", include=["yandexcloud*", "yandex*"])

__version__ = "0.257.0"

setup(
    name="yandexcloud",
    version=__version__,
    description="The Yandex.Cloud official SDK",
    url="https://github.com/yandex-cloud/python-sdk",
    author="Yandex LLC",
    author_email="cloud@support.yandex.ru",
    license="MIT",
    install_requires=[
        "cryptography>=2.8",
        "grpcio>=1.56.2",
        "protobuf>=4.23.4",
        "googleapis-common-protos>=1.59.1",
        "pyjwt>=1.7.1",
        "requests>=2.22.0",
        "six>=1.14.0",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    tests_require=["pytest"],
    packages=packages,
    zip_safe=False,
)
