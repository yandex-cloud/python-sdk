from setuptools import setup, find_packages

packages = find_packages('.', include=['yandexcloud*', 'yandex*'])

setup(name='yandexcloud',
      version='0.9.0',
      description='The Yandex.Cloud official SDK',
      url='https://github.com/yandex-cloud/python-sdk',
      author='Yandex LLC',
      author_email='cloud@support.yandex.ru',
      license='MIT',
      install_requires=[
          'cryptography',
          'grpcio>=0.17.0',
          'googleapis-common-protos',
          'pyjwt',
          'six',
      ],
      tests_require=['pytest'],
      packages=packages,
      zip_safe=False)
