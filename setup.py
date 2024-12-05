from setuptools import setup, find_packages

setup(
    name='one_key',
    version='1.0.0',
    author='Hubert Dang',
    author_email='hubertdang@gmail.com',
    description='A command line password manager',
    long_description=open('README.md').read(),
    url='https://github.com/hubertdang/one-key',
    packages=find_packages(exclude=['test', 'testpypi', 'build', 'one_key.egg-info']),
    entry_points={
        'console_scripts': [
            'one_key=one_key.one_key:main',
        ],
    },
)
