from setuptools import setup, find_packages

setup(
    name='one_key',
    version='1.0.0',
    author='Hubert Dang',
    author_email='hubertdang@gmail.com',
    description='A command line password manager',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts': [
            'one_key=one_key.one_key:main',
        ],
    },
)
