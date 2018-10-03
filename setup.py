from setuptools import setup, find_packages

packages = find_packages('.',
    include=['yandexcloud*', 'yandex*'])

setup(name='yandexcloud',
    version='0.3',
    description='The Yandex.Cloud official SDK',
    url='https://github.com/yandex-cloud/python-sdk',
    author='Yandex LLC',
    author_email='FIXME',
    license='MIT',
    install_requires=[
        'grpcio',
        'googleapis-common-protos',
    ],
    packages=packages,
    zip_safe=False)
