from setuptools import setup, find_packages

packages = find_packages('.', include=['yandexcloud*', 'yandex*'])

__version__ = "0.133.0"


setup(name='yandexcloud',
      version=__version__,
      description='The Yandex.Cloud official SDK',
      url='https://github.com/yandex-cloud/python-sdk',
      author='Yandex LLC',
      author_email='cloud@support.yandex.ru',
      license='MIT',
      install_requires=[
          'cryptography>=2.8',
          'grpcio>=1.38.1',
          'googleapis-common-protos>=1.53.0',
          'pyjwt>=1.7.1',
          'requests>=2.22.0',
          'six>=1.14.0',
      ],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
      ],
      tests_require=['pytest'],
      packages=packages,
      zip_safe=False)
