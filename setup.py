from setuptools import setup

setup(
    packages=['jenklint'],
    zip_safe=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            'jenklint = jenklint.__main__:main'
        ]
    },
)
