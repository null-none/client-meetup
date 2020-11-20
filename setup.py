from setuptools import setup, find_packages

setup(
    name='client_meeetup',
    version='0.0.2',
    packages=find_packages(),
    author='Dmitry Kalinin',
    url='https://github.com/null-none/client-meetup',
    install_requires=[
        'requests',
    ],
)
