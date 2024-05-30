from setuptools import find_packages, setup

packages = find_packages(".", include=["yandexcloud*", "yandex*"])

__version__ = "0.287.0"

with open("README.md") as file:
    README = file.read()

setup(
    name="yandexcloud",
    version=__version__,
    description="The Yandex.Cloud official SDK",
    url="https://github.com/yandex-cloud/python-sdk",
    author="Yandex LLC",
    author_email="cloud@support.yandex.ru",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=[
        "cryptography>=2.8",
        "grpcio>=1.64.0",
        "protobuf>=4.25.3",
        "googleapis-common-protos>=1.63.0",
        "pyjwt>=1.7.1",
        "requests>=2.22.0",
        "six>=1.14.0",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    tests_require=["pytest"],
    packages=packages,
    zip_safe=False,
)
