from setuptools import setup

setup(
    packages=['jenklint'],
    zip_safe=True,
    entry_points={
        "console_scripts": [
            'jenklint = jenklint.__main__:main'
        ]
    },
)
