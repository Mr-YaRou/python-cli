from setuptools import setup
setup(
    name = 'pytest',
    version = '0.1.0',
    packages = ['pytest'],
    entry_points = {
        'console_scripts': [
            'pytest = pytest.__main__:main'
        ]
    })