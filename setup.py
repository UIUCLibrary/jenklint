from setuptools import setup

setup(
    packages=['jenklint'],
    entry_points={
        "console_scripts": [
            'jenklint = jenklint.__main__:main'
        ]
    },
)
