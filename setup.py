from setuptools import setup, find_packages

setup(
    name="one_key",
    version="1.0.0",
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts': [
            'one_key=one_key.one_key:main',
        ],
    },
)
